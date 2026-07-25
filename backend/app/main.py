from typing import List

import os
from random import Random

from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np

from .models import ErrorMessage, GuessResult, Champion, LocalName
from .similarity import calculate_ranks

if "LOLMANTLE_CHAMPIONS" not in os.environ:
    os.environ["LOLMANTLE_CHAMPIONS"] = "/data/champions.csv"

if "LOLMANTLE_NAME_MAP" not in os.environ:
    os.environ["LOLMANTLE_NAME_MAP"] = "/data/name_map.csv"

RANDOM = Random(os.environ.get("LOLMANTLE_RANDOM_SEED", 20260725))

# Use the environment variables, fallback to local paths if running outside docker
champions_path = os.environ.get("LOLMANTLE_CHAMPIONS", "../data/champions.csv")
name_map_path = os.environ.get("LOLMANTLE_NAME_MAP", "../data/name_map.csv")

if not os.path.exists(champions_path):
    champions_path = os.path.join(os.path.dirname(__file__), '../../data/champions.csv')
if not os.path.exists(name_map_path):
    name_map_path = os.path.join(os.path.dirname(__file__), '../../data/name_map.csv')

CHAMPIONS = pd.read_csv(champions_path).replace({np.nan: None})
CHAMPION_NAME_MAP = pd.read_csv(name_map_path)

CHAMPION_SIZE = len(CHAMPIONS.index)
SECRET_INDEXES = RANDOM.sample(range(CHAMPION_SIZE), k=CHAMPION_SIZE)

app = FastAPI(
    docs_url=None if os.environ.get("LOLMANTLE_PRODUCTION", False) else "/docs",
    redoc_url=None,
)

if not os.environ.get("LOLMANTLE_PRODUCTION", False):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            os.environ.get("LOLMANTLE_CORS_ORIGIN", "http://localhost:3000")
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def secret_index(puzzle_number: int) -> int:
    return SECRET_INDEXES[puzzle_number % CHAMPION_SIZE]


@app.get(
    "/languages",
    response_model=List[str],
    responses={
        200: {
            "content": {"application/json": {"example": ["english_name", "local_name"]}},
        },
    },
)
async def languages():
    """The list of all languages"""
    return [name for name in CHAMPION_NAME_MAP.columns]


@app.get(
    "/champions",
    response_model=List[Champion],
)
async def champions():
    """The list of all Champions"""
    return [CHAMPIONS.loc[i].to_dict() for i in CHAMPIONS.index]


@app.get(
    "/champion_name_map/{language}",
    response_model=List[LocalName],
)
async def champion_name_map(
    language: str = Path(..., description="The language to use", example="local_name"),
):
    """The list of all Champion's local names"""

    col = "local_name" if language == "ko" else "english_name"
    items = [CHAMPION_NAME_MAP.loc[i] for i in CHAMPION_NAME_MAP.index]
    return [
        LocalName(
            english_name=item["english_name"],
            local_name=item[col],
        )
        for item in items
    ]


@app.get(
    "/rank/{puzzle_number}",
    response_model=List[GuessResult],
)
async def rank(
    puzzle_number: int = Path(..., description="Number of Lolmantle.", example=1),
):
    """Similarity ranking"""
    index = secret_index(puzzle_number)
    ranks = calculate_ranks(
        champion_index=index,
        champions=CHAMPIONS,
    )
    return ranks


def normalize_champion_name(s) -> str:
    if s is None or pd.isna(s):
        return ""
    import re
    return re.sub(r"[^a-zA-Z0-9가-힣]", "", str(s)).lower()

@app.get(
    "/guess/{puzzle_number}",
    response_model=GuessResult,
    responses={
        404: {
            "model": ErrorMessage,
            "description": "Champion not found.",
            "content": {
                "application/json": {
                    "example": {
                        "code": ErrorMessage.CodeConstant.CODE_CHAMPION_NOT_FOUND,
                        "message": "Champion not found.",
                    }
                }
            },
        }
    },
)
async def guess(
    puzzle_number: int = Path(..., description="Number of Lolmantle.", example=1),
    name: str = Query(..., description="Champion's English or Korean name or alias.", example="Annie"),
):
    """Guess the Champion"""
    index = secret_index(puzzle_number)
    ranks = calculate_ranks(
        champion_index=index,
        champions=CHAMPIONS,
    )

    clean_target = normalize_champion_name(name)
    if not clean_target:
        return JSONResponse(
            status_code=404,
            content=ErrorMessage(
                code=ErrorMessage.CodeConstant.CODE_CHAMPION_NOT_FOUND,
                message="Champion not found.",
            ).dict(),
        )

    # 1. Direct match on guess_result.name
    for guess_result in ranks:
        if normalize_champion_name(guess_result.name) == clean_target:
            return guess_result

    # 2. Check against CHAMPIONS dataset columns (name_en, name_ko, alias)
    matched_index = None
    for idx, row in CHAMPIONS.iterrows():
        n_en = normalize_champion_name(row.get('name_en'))
        n_ko = normalize_champion_name(row.get('name_ko'))
        n_alias = normalize_champion_name(row.get('alias'))
        if clean_target in (n_en, n_ko, n_alias) or n_en.startswith(clean_target) or n_alias.startswith(clean_target):
            matched_index = idx
            break

    # 3. Check against CHAMPION_NAME_MAP (english_name, local_name)
    if matched_index is None:
        for _, row in CHAMPION_NAME_MAP.iterrows():
            n_eng = normalize_champion_name(row.get('english_name'))
            n_loc = normalize_champion_name(row.get('local_name'))
            if clean_target in (n_eng, n_loc):
                for idx, c_row in CHAMPIONS.iterrows():
                    if normalize_champion_name(c_row.get('name_en')) == n_eng or normalize_champion_name(c_row.get('alias')) == n_eng:
                        matched_index = idx
                        break
                break

    if matched_index is not None:
        target_name_en = CHAMPIONS.loc[matched_index].get('name_en') or CHAMPIONS.loc[matched_index].get('alias')
        for guess_result in ranks:
            if normalize_champion_name(guess_result.name) == normalize_champion_name(target_name_en):
                return guess_result

    return JSONResponse(
        status_code=404,
        content=ErrorMessage(
            code=ErrorMessage.CodeConstant.CODE_CHAMPION_NOT_FOUND,
            message="Champion not found.",
        ).dict(),
    )
