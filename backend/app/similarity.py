from typing import List
import pandas as pd
import math
from .models import GuessResult

# 18개 스탯 항목별 DiffMax 사전 정의 (crit 제외, 비에고 마나 정제 반영)
STAT_DIFF_MAX = {
    'hp_base': 286.0,
    'hp_max': 1069.0,
    'mp_base': 530.0,
    'mp_max': 1879.0,
    'movespeed': 40.0,
    'armor_base': 25.0,
    'armor_max': 93.65,
    'spellblock_base': 15.0,
    'spellblock_max': 31.65,
    'attackrange': 525.0,
    'hpregen_base': 10.0,
    'hpregen_max': 27.0,
    'mpregen_base': 50.0,
    'mpregen_max': 50.0,
    'attackdamage_base': 25.0,
    'attackdamage_max': 25.0,
    'attackspeed_base': 0.375,
    'attackspeed_max': 0.6375,
}

def calculate_similarity_detail(champ1, champ2) -> dict:
    """
    Hybrid Weighted Similarity Algorithm.
    Category Total: 80 pts (7 items, 80/7 pts each)
    Stat Total: 20 pts (18 items, 20/18 pts each using Min-Max scaling)
    Total: 100 pts -> normalized to 0.0 ~ 1.0
    """
    category_score = 0.0
    cat_unit_score = 80.0 / 7.0  # ~11.428 pts per category item (7 items total)

    # 1. Region (소속 지역)
    if champ1.get('region') and champ2.get('region') and champ1['region'] == champ2['region']:
        category_score += cat_unit_score

    # 2. Role / Tags (주 역할군 tag_1 + 부 역할군 tag_2 고려)
    t1_1 = champ1.get('tag_1') if pd.notna(champ1.get('tag_1')) else None
    t1_2 = champ1.get('tag_2') if pd.notna(champ1.get('tag_2')) else None
    t2_1 = champ2.get('tag_1') if pd.notna(champ2.get('tag_1')) else None
    t2_2 = champ2.get('tag_2') if pd.notna(champ2.get('tag_2')) else None

    if t1_1 and t2_1:
        if t1_1 == t2_1 and t1_2 == t2_2:
            # 주역할군 & 부역할군 모두 완벽 일치 -> 만점 (100%)
            category_score += cat_unit_score * 1.0
        elif t1_1 == t2_1:
            # 주역할군만 동일 -> 80%
            category_score += cat_unit_score * 0.8
        elif t1_1 == t2_2 and t1_2 == t2_1:
            # 주역할군과 부역할군 교차 완전 일치 -> 70%
            category_score += cat_unit_score * 0.7
        elif (t1_1 == t2_2 or t1_2 == t2_1 or (t1_2 and t2_2 and t1_2 == t2_2)):
            # 부역할군 부분 일치 -> 50%
            category_score += cat_unit_score * 0.5

    # 3. Attack Type (근거리 / 원거리)
    if champ1.get('attack_type') and champ2.get('attack_type') and champ1['attack_type'] == champ2['attack_type']:
        category_score += cat_unit_score

    # 4. Resource Type (partype: 마나, 기력, 노마나 등)
    if champ1.get('partype') and champ2.get('partype') and champ1['partype'] == champ2['partype']:
        category_score += cat_unit_score

    # 5. Species (종족)
    if champ1.get('species') and champ2.get('species') and champ1['species'] == champ2['species']:
        category_score += cat_unit_score

    # 6. Gender (성별)
    if champ1.get('gender') and champ2.get('gender') and champ1['gender'] == champ2['gender']:
        category_score += cat_unit_score

    # 7. Release Order (champion_id min-max)
    try:
        id1 = float(champ1.get('champion_id', 0))
        id2 = float(champ2.get('champion_id', 0))
        if id1 > 0 and id2 > 0:
            diff = abs(id1 - id2)
            max_id_diff = 172.0  # Max possible difference (173 - 1)
            ratio = max(0.0, 1.0 - (diff / max_id_diff))
            category_score += cat_unit_score * ratio
    except (ValueError, TypeError):
        pass

    # Stat Score (20 pts max across 18 stat columns)
    stat_score = 0.0
    stat_unit_score = 20.0 / len(STAT_DIFF_MAX)  # 20 / 18 = ~1.1111 pts per stat

    for stat_col, diff_max in STAT_DIFF_MAX.items():
        try:
            val1 = float(champ1[stat_col])
            val2 = float(champ2[stat_col])
            diff = abs(val1 - val2)
            ratio = max(0.0, 1.0 - (diff / diff_max)) if diff_max > 0 else 1.0
            stat_score += stat_unit_score * ratio
        except (ValueError, TypeError, KeyError):
            continue

    total_score = (category_score + stat_score) / 100.0
    sim = round(min(1.0, max(0.0, total_score)), 6)
    cat_round = round(category_score, 1)
    stat_round = round(stat_score, 1)

    return {
        'similarity': sim,
        'category_score': cat_round,
        'stat_score': stat_round,
        'formula_detail': f"카테고리 {cat_round}점 + 스탯 {stat_round}점"
    }


def calculate_similarity(champ1, champ2) -> float:
    return calculate_similarity_detail(champ1, champ2)['similarity']


def calculate_ranks(champion_index: int, champions: pd.DataFrame) -> List[GuessResult]:
    target_champ = champions.loc[champion_index]
    ranks = []

    for i in champions.index:
        champ = champions.loc[i]
        detail = calculate_similarity_detail(target_champ, champ)
        sim = detail['similarity']
        if i == champion_index:
            sim = 1.0
            detail['category_score'] = 80.0
            detail['stat_score'] = 20.0
            detail['formula_detail'] = "카테고리 80.0점 + 스탯 20.0점"

        champ_name = champ.get('name_en') if 'name_en' in champ and pd.notna(champ['name_en']) else champ.get('name', champ.get('alias'))
        ranks.append({
            'name': champ_name,
            'similarity': sim,
            'category_score': detail['category_score'],
            'stat_score': detail['stat_score'],
            'formula_detail': detail['formula_detail'],
            'index': i
        })

    ranks.sort(key=lambda x: x['similarity'], reverse=True)

    results = []
    for rank_idx, item in enumerate(ranks, start=1):
        results.append(GuessResult(
            rank=rank_idx,
            name=str(item['name']),
            similarity=float(item['similarity']),
            category_score=float(item['category_score']),
            stat_score=float(item['stat_score']),
            formula_detail=str(item['formula_detail'])
        ))
    return results
