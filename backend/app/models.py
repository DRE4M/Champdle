from typing import Optional
from pydantic import BaseModel, Field


class Champion(BaseModel):
    champion_id: int = Field(..., example=1)
    riot_id: int = Field(..., example=1)
    alias: str = Field(..., example="Annie")
    name_en: str = Field(..., example="Annie")
    name_ko: str = Field(..., example="애니")
    title_en: str = Field(..., example="the Dark Child")
    title_ko: str = Field(..., example="어둠의 아이")
    gender: str = Field(..., example="Female")
    species: str = Field(..., example="Human")
    region: str = Field(..., example="Noxus")
    attack_type: str = Field(..., example="ranged")
    tag_1: str = Field(..., example="Mage")
    tag_2: Optional[str] = Field(None, example="Support")
    partype: Optional[str] = Field(None, example="Mana")
    hp_base: float = Field(..., example=560)
    hp_max: float = Field(..., example=2192)
    mp_base: float = Field(..., example=418)
    mp_max: float = Field(..., example=843)
    movespeed: float = Field(..., example=335)
    armor_base: float = Field(..., example=23)
    armor_max: float = Field(..., example=91)
    spellblock_base: float = Field(..., example=30)
    spellblock_max: float = Field(..., example=52.1)
    attackrange: float = Field(..., example=625)
    hpregen_base: float = Field(..., example=5.5)
    hpregen_max: float = Field(..., example=14.85)
    mpregen_base: float = Field(..., example=8.0)
    mpregen_max: float = Field(..., example=21.6)
    crit_base: float = Field(..., example=0.0)
    crit_max: float = Field(..., example=0.0)
    attackdamage_base: float = Field(..., example=50)
    attackdamage_max: float = Field(..., example=50)
    attackspeed_base: float = Field(..., example=0.61)
    attackspeed_max: float = Field(..., example=0.751)
    image_path: str = Field(..., example='1.png')


class LocalName(BaseModel):
    english_name: str = Field(..., example="Annie")
    local_name: str = Field(..., example="애니")


class ErrorMessage(BaseModel):
    code: int = Field(..., example=11)
    message: str = Field(..., example="Champion not found.")

    class CodeConstant:
        CODE_CHAMPION_NOT_FOUND = 11


class GuessResult(BaseModel):
    name: str = Field(..., example="Annie")
    rank: int = Field(..., example=1)
    similarity: float = Field(..., example=1.0)
