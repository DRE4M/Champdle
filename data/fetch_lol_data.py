import urllib.request
import json
import csv
import os
import concurrent.futures

# Comprehensive Metadata Map (Gender, Species, Region)
CHAMPION_METADATA = {
    'Aatrox': {'gender': 'Male', 'species': 'Darkin', 'region': 'Runeterra'},
    'Ahri': {'gender': 'Female', 'species': 'Vastaya', 'region': 'Ionia'},
    'Akali': {'gender': 'Female', 'species': 'Human', 'region': 'Ionia'},
    'Akshan': {'gender': 'Male', 'species': 'Human', 'region': 'Shurima'},
    'Alistar': {'gender': 'Male', 'species': 'Minotaur', 'region': 'Runeterra'},
    'Ambessa': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'Amumu': {'gender': 'Male', 'species': 'Yordle', 'region': 'Shurima'},
    'Anivia': {'gender': 'Female', 'species': 'Spirit / God', 'region': 'Freljord'},
    'Annie': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'Aphelios': {'gender': 'Male', 'species': 'Human', 'region': 'Targon'},
    'Ashe': {'gender': 'Female', 'species': 'Human', 'region': 'Freljord'},
    'AurelionSol': {'gender': 'Male', 'species': 'Dragon', 'region': 'Targon'},
    'Aurora': {'gender': 'Female', 'species': 'Vastaya', 'region': 'Freljord'},
    'Azir': {'gender': 'Male', 'species': 'God-Warrior / Ascended', 'region': 'Shurima'},
    'Bard': {'gender': 'Male', 'species': 'Celestial', 'region': 'Runeterra'},
    'Belveth': {'gender': 'Female', 'species': 'VoidBorn', 'region': 'The Void'},
    'Blitzcrank': {'gender': 'Other', 'species': 'Cyborg / Mech', 'region': 'Zaun'},
    'Brand': {'gender': 'Male', 'species': 'Human / Elemental', 'region': 'Freljord'},
    'Braum': {'gender': 'Male', 'species': 'Human', 'region': 'Freljord'},
    'Briar': {'gender': 'Female', 'species': 'Construct / Golem', 'region': 'Noxus'},
    'Caitlyn': {'gender': 'Female', 'species': 'Human', 'region': 'Piltover'},
    'Camille': {'gender': 'Female', 'species': 'Cyborg / Mech', 'region': 'Piltover'},
    'Cassiopeia': {'gender': 'Female', 'species': 'Human / Serpent', 'region': 'Noxus'},
    'Chogath': {'gender': 'Male', 'species': 'VoidBorn', 'region': 'The Void'},
    'Corki': {'gender': 'Male', 'species': 'Yordle', 'region': 'Bandle City'},
    'Darius': {'gender': 'Male', 'species': 'Human', 'region': 'Noxus'},
    'Diana': {'gender': 'Female', 'species': 'Human', 'region': 'Targon'},
    'Draven': {'gender': 'Male', 'species': 'Human', 'region': 'Noxus'},
    'DrMundo': {'gender': 'Male', 'species': 'Human', 'region': 'Zaun'},
    'Ekko': {'gender': 'Male', 'species': 'Human', 'region': 'Zaun'},
    'Elise': {'gender': 'Female', 'species': 'Human / Spider', 'region': 'Noxus'},
    'Evelynn': {'gender': 'Female', 'species': 'Demon', 'region': 'Runeterra'},
    'Ezreal': {'gender': 'Male', 'species': 'Human', 'region': 'Piltover'},
    'FiddleSticks': {'gender': 'Other', 'species': 'Demon', 'region': 'Runeterra'},
    'Fiora': {'gender': 'Female', 'species': 'Human', 'region': 'Demacia'},
    'Fizz': {'gender': 'Male', 'species': 'Yordle', 'region': 'Bilgewater'},
    'Galio': {'gender': 'Male', 'species': 'Construct / Golem', 'region': 'Demacia'},
    'Gangplank': {'gender': 'Male', 'species': 'Human', 'region': 'Bilgewater'},
    'Garen': {'gender': 'Male', 'species': 'Human', 'region': 'Demacia'},
    'Gnar': {'gender': 'Male', 'species': 'Yordle', 'region': 'Freljord'},
    'Gragas': {'gender': 'Male', 'species': 'Human', 'region': 'Freljord'},
    'Graves': {'gender': 'Male', 'species': 'Human', 'region': 'Bilgewater'},
    'Gwen': {'gender': 'Female', 'species': 'Human / Doll', 'region': 'Shadow Isles'},
    'Hecarim': {'gender': 'Male', 'species': 'Undead / Spirit', 'region': 'Shadow Isles'},
    'Heimerdinger': {'gender': 'Male', 'species': 'Yordle', 'region': 'Piltover'},
    'Hwei': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Illaoi': {'gender': 'Female', 'species': 'Human', 'region': 'Bilgewater'},
    'Irelia': {'gender': 'Female', 'species': 'Human', 'region': 'Ionia'},
    'Ivern': {'gender': 'Male', 'species': 'Human / Tree', 'region': 'Ionia'},
    'Janna': {'gender': 'Female', 'species': 'Spirit / God', 'region': 'Zaun'},
    'JarvanIV': {'gender': 'Male', 'species': 'Human', 'region': 'Demacia'},
    'Jax': {'gender': 'Male', 'species': 'Human', 'region': 'Icathia'},
    'Jayce': {'gender': 'Male', 'species': 'Human', 'region': 'Piltover'},
    'Jhin': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Jinx': {'gender': 'Female', 'species': 'Human', 'region': 'Zaun'},
    'Kaisa': {'gender': 'Female', 'species': 'Human', 'region': 'The Void'},
    'Kalista': {'gender': 'Female', 'species': 'Undead / Spirit', 'region': 'Shadow Isles'},
    'Karma': {'gender': 'Female', 'species': 'Human', 'region': 'Ionia'},
    'Karthus': {'gender': 'Male', 'species': 'Undead / Spirit', 'region': 'Shadow Isles'},
    'Kassadin': {'gender': 'Male', 'species': 'Human', 'region': 'The Void'},
    'Katarina': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'Kayle': {'gender': 'Female', 'species': 'Celestial', 'region': 'Demacia'},
    'Kayn': {'gender': 'Male', 'species': 'Human / Darkin', 'region': 'Ionia'},
    'Kennen': {'gender': 'Male', 'species': 'Yordle', 'region': 'Ionia'},
    'Khazix': {'gender': 'Male', 'species': 'VoidBorn', 'region': 'The Void'},
    'Kindred': {'gender': 'Other', 'species': 'Spirit / God', 'region': 'Runeterra'},
    'Kled': {'gender': 'Male', 'species': 'Yordle', 'region': 'Noxus'},
    'KogMaw': {'gender': 'Male', 'species': 'VoidBorn', 'region': 'The Void'},
    'KSante': {'gender': 'Male', 'species': 'Human', 'region': 'Shurima'},
    'Leblanc': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'LeeSin': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Leona': {'gender': 'Female', 'species': 'Human', 'region': 'Targon'},
    'Lillia': {'gender': 'Female', 'species': 'Spirit', 'region': 'Ionia'},
    'Lissandra': {'gender': 'Female', 'species': 'Human', 'region': 'Freljord'},
    'Lucian': {'gender': 'Male', 'species': 'Human', 'region': 'Demacia'},
    'Lulu': {'gender': 'Female', 'species': 'Yordle', 'region': 'Bandle City'},
    'Lux': {'gender': 'Female', 'species': 'Human', 'region': 'Demacia'},
    'Malphite': {'gender': 'Male', 'species': 'Construct / Golem', 'region': 'Ixtal'},
    'Malzahar': {'gender': 'Male', 'species': 'Human', 'region': 'The Void'},
    'Maokai': {'gender': 'Male', 'species': 'Spirit / Tree', 'region': 'Shadow Isles'},
    'MasterYi': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Milio': {'gender': 'Male', 'species': 'Human', 'region': 'Ixtal'},
    'MissFortune': {'gender': 'Female', 'species': 'Human', 'region': 'Bilgewater'},
    'MonkeyKing': {'gender': 'Male', 'species': 'Vastaya', 'region': 'Ionia'},
    'Mordekaiser': {'gender': 'Male', 'species': 'Undead / Spirit', 'region': 'Noxus'},
    'Morgana': {'gender': 'Female', 'species': 'Celestial', 'region': 'Demacia'},
    'Naafiri': {'gender': 'Female', 'species': 'Darkin', 'region': 'Shurima'},
    'Nami': {'gender': 'Female', 'species': 'Vastaya', 'region': 'Runeterra'},
    'Nasus': {'gender': 'Male', 'species': 'God-Warrior / Ascended', 'region': 'Shurima'},
    'Nautilus': {'gender': 'Male', 'species': 'Undead / Cyborg', 'region': 'Bilgewater'},
    'Neeko': {'gender': 'Female', 'species': 'Vastaya', 'region': 'Ixtal'},
    'Nidalee': {'gender': 'Female', 'species': 'Human', 'region': 'Ixtal'},
    'Nilah': {'gender': 'Female', 'species': 'Human', 'region': 'Bilgewater'},
    'Nocturne': {'gender': 'Male', 'species': 'Demon', 'region': 'Runeterra'},
    'Nunu': {'gender': 'Male', 'species': 'Human', 'region': 'Freljord'},
    'Olaf': {'gender': 'Male', 'species': 'Human', 'region': 'Freljord'},
    'Orianna': {'gender': 'Female', 'species': 'Cyborg / Mech', 'region': 'Piltover'},
    'Ornn': {'gender': 'Male', 'species': 'Spirit / God', 'region': 'Freljord'},
    'Pantheon': {'gender': 'Male', 'species': 'Human / Celestial', 'region': 'Targon'},
    'Poppy': {'gender': 'Female', 'species': 'Yordle', 'region': 'Demacia'},
    'Pyke': {'gender': 'Male', 'species': 'Undead', 'region': 'Bilgewater'},
    'Qiyana': {'gender': 'Female', 'species': 'Human', 'region': 'Ixtal'},
    'Quinn': {'gender': 'Female', 'species': 'Human', 'region': 'Demacia'},
    'Rakan': {'gender': 'Male', 'species': 'Vastaya', 'region': 'Ionia'},
    'Rammus': {'gender': 'Male', 'species': 'Ascended', 'region': 'Shurima'},
    'RekSai': {'gender': 'Female', 'species': 'VoidBorn', 'region': 'The Void'},
    'Rell': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'Renata': {'gender': 'Female', 'species': 'Human', 'region': 'Zaun'},
    'Renekton': {'gender': 'Male', 'species': 'God-Warrior / Ascended', 'region': 'Shurima'},
    'Rengar': {'gender': 'Male', 'species': 'Vastaya', 'region': 'Ixtal'},
    'Riven': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'Rumble': {'gender': 'Male', 'species': 'Yordle', 'region': 'Bandle City'},
    'Ryze': {'gender': 'Male', 'species': 'Human', 'region': 'Runeterra'},
    'Samira': {'gender': 'Female', 'species': 'Human', 'region': 'Noxus'},
    'Sejuani': {'gender': 'Female', 'species': 'Human', 'region': 'Freljord'},
    'Senna': {'gender': 'Female', 'species': 'Human / Spirit', 'region': 'Shadow Isles'},
    'Seraphine': {'gender': 'Female', 'species': 'Human', 'region': 'Piltover'},
    'Sett': {'gender': 'Male', 'species': 'Human / Vastaya', 'region': 'Ionia'},
    'Shaco': {'gender': 'Male', 'species': 'Demon', 'region': 'Runeterra'},
    'Shen': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Shyvana': {'gender': 'Female', 'species': 'Dragon', 'region': 'Demacia'},
    'Singed': {'gender': 'Male', 'species': 'Human', 'region': 'Zaun'},
    'Sion': {'gender': 'Male', 'species': 'Undead', 'region': 'Noxus'},
    'Sivir': {'gender': 'Female', 'species': 'Human', 'region': 'Shurima'},
    'Skarner': {'gender': 'Male', 'species': 'Brackern / Elemental', 'region': 'Ixtal'},
    'Smolder': {'gender': 'Male', 'species': 'Dragon', 'region': 'Camavor'},
    'Sona': {'gender': 'Female', 'species': 'Human', 'region': 'Demacia'},
    'Soraka': {'gender': 'Female', 'species': 'Celestial', 'region': 'Targon'},
    'Swain': {'gender': 'Male', 'species': 'Human', 'region': 'Noxus'},
    'Sylas': {'gender': 'Male', 'species': 'Human', 'region': 'Demacia'},
    'Syndra': {'gender': 'Female', 'species': 'Human', 'region': 'Ionia'},
    'TahmKench': {'gender': 'Male', 'species': 'Demon', 'region': 'Bilgewater'},
    'Taliyah': {'gender': 'Female', 'species': 'Human', 'region': 'Shurima'},
    'Talon': {'gender': 'Male', 'species': 'Human', 'region': 'Noxus'},
    'Taric': {'gender': 'Male', 'species': 'Human / Celestial', 'region': 'Targon'},
    'Teemo': {'gender': 'Male', 'species': 'Yordle', 'region': 'Bandle City'},
    'Thresh': {'gender': 'Male', 'species': 'Undead', 'region': 'Shadow Isles'},
    'Tristana': {'gender': 'Female', 'species': 'Yordle', 'region': 'Bandle City'},
    'Trundle': {'gender': 'Male', 'species': 'Troll', 'region': 'Freljord'},
    'Tryndamere': {'gender': 'Male', 'species': 'Human', 'region': 'Freljord'},
    'TwistedFate': {'gender': 'Male', 'species': 'Human', 'region': 'Bilgewater'},
    'Twitch': {'gender': 'Male', 'species': 'Rat / Mutant', 'region': 'Zaun'},
    'Udyr': {'gender': 'Male', 'species': 'Human', 'region': 'Freljord'},
    'Urgot': {'gender': 'Male', 'species': 'Human / Cyborg', 'region': 'Zaun'},
    'Varus': {'gender': 'Male', 'species': 'Darkin', 'region': 'Ionia'},
    'Vayne': {'gender': 'Female', 'species': 'Human', 'region': 'Demacia'},
    'Veigar': {'gender': 'Male', 'species': 'Yordle', 'region': 'Bandle City'},
    'Velkoz': {'gender': 'Male', 'species': 'VoidBorn', 'region': 'The Void'},
    'Vex': {'gender': 'Female', 'species': 'Yordle', 'region': 'Shadow Isles'},
    'Vi': {'gender': 'Female', 'species': 'Human', 'region': 'Piltover'},
    'Viego': {'gender': 'Male', 'species': 'Undead', 'region': 'Shadow Isles'},
    'Viktor': {'gender': 'Male', 'species': 'Cyborg / Mech', 'region': 'Zaun'},
    'Vladimir': {'gender': 'Male', 'species': 'Human', 'region': 'Noxus'},
    'Volibear': {'gender': 'Male', 'species': 'Spirit / God', 'region': 'Freljord'},
    'Warwick': {'gender': 'Male', 'species': 'Human / Mutant', 'region': 'Zaun'},
    'Xerath': {'gender': 'Male', 'species': 'God-Warrior / Ascended', 'region': 'Shurima'},
    'XinZhao': {'gender': 'Male', 'species': 'Human', 'region': 'Demacia'},
    'Xayah': {'gender': 'Female', 'species': 'Vastaya', 'region': 'Ionia'},
    'Yasuo': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Yone': {'gender': 'Male', 'species': 'Human / Spirit', 'region': 'Ionia'},
    'Yorick': {'gender': 'Male', 'species': 'Human', 'region': 'Shadow Isles'},
    'Yuumi': {'gender': 'Female', 'species': 'Cat / Magical', 'region': 'Bandle City'},
    'Zac': {'gender': 'Male', 'species': 'Mutant / Ooze', 'region': 'Zaun'},
    'Zed': {'gender': 'Male', 'species': 'Human', 'region': 'Ionia'},
    'Zeri': {'gender': 'Female', 'species': 'Human', 'region': 'Zaun'},
    'Ziggs': {'gender': 'Male', 'species': 'Yordle', 'region': 'Zaun'},
    'Zilean': {'gender': 'Male', 'species': 'Human', 'region': 'Icathia'},
    'Zoe': {'gender': 'Female', 'species': 'Human / Celestial', 'region': 'Targon'},
    'Zyra': {'gender': 'Female', 'species': 'Plant / Spirit', 'region': 'Ixtal'}
}

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

def download_file(url, local_path):
    if not os.path.exists(local_path):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())

def fetch_champ_detail(riot_id):
    cd_detail_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/{riot_id}.json"
    cd_detail_ko_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/ko_kr/v1/champions/{riot_id}.json"
    
    cd_detail, cd_detail_ko = {}, {}
    try:
        cd_detail = fetch_json(cd_detail_url)
    except Exception as e:
        pass
    try:
        cd_detail_ko = fetch_json(cd_detail_ko_url)
    except Exception as e:
        pass
    return riot_id, cd_detail, cd_detail_ko

def main():
    data_dir = os.path.dirname(os.path.abspath(__file__))
    raw_dir = os.path.join(data_dir, 'raw')
    image_dir = os.path.join(data_dir, '..', 'images')
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    print("1. Fetching DDragon versions...")
    versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    versions = fetch_json(versions_url)
    latest_version = versions[0]
    print(f"Latest LoL Version: {latest_version}")

    with open(os.path.join(raw_dir, 'versions.json'), 'w', encoding='utf-8') as f:
        json.dump(versions, f, ensure_ascii=False, indent=2)

    print("2. Fetching DDragon championFull.json (en_US & ko_KR)...")
    en_ddragon_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/championFull.json"
    ko_ddragon_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/ko_KR/championFull.json"

    en_ddragon_raw = fetch_json(en_ddragon_url)
    ko_ddragon_raw = fetch_json(ko_ddragon_url)

    with open(os.path.join(raw_dir, 'ddragon_championFull_en.json'), 'w', encoding='utf-8') as f:
        json.dump(en_ddragon_raw, f, ensure_ascii=False, indent=2)
    with open(os.path.join(raw_dir, 'ddragon_championFull_ko.json'), 'w', encoding='utf-8') as f:
        json.dump(ko_ddragon_raw, f, ensure_ascii=False, indent=2)

    en_ddragon_map = en_ddragon_raw['data']
    ko_ddragon_map = ko_ddragon_raw['data']

    print("3. Fetching CDragon champion summary...")
    cdragon_summary_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json"
    cdragon_summary_ko_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/ko_kr/v1/champion-summary.json"

    cdragon_summary = fetch_json(cdragon_summary_url)
    cdragon_summary_ko = fetch_json(cdragon_summary_ko_url)

    with open(os.path.join(raw_dir, 'cdragon_champion_summary_en.json'), 'w', encoding='utf-8') as f:
        json.dump(cdragon_summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(raw_dir, 'cdragon_champion_summary_ko.json'), 'w', encoding='utf-8') as f:
        json.dump(cdragon_summary_ko, f, ensure_ascii=False, indent=2)

    valid_cdragon_champs = [c for c in cdragon_summary if c.get('id') and c['id'] > 0]
    valid_cdragon_champs.sort(key=lambda c: c['id'])

    print(f"4. Parallel fetching details for {len(valid_cdragon_champs)} champions...")
    details_map = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_id = {executor.submit(fetch_champ_detail, c['id']): c['id'] for c in valid_cdragon_champs}
        for future in concurrent.futures.as_completed(future_to_id):
            r_id, cd_detail, cd_detail_ko = future.result()
            details_map[r_id] = (cd_detail, cd_detail_ko)

    champions_csv = []
    name_map_csv = []
    raw_details = {}

    print("5. Processing and generating champions.csv & name_map.csv...")
    for order_idx, cd_champ in enumerate(valid_cdragon_champs, start=1):
        riot_id = cd_champ['id']
        alias = cd_champ['alias']

        dd_alias = alias
        if dd_alias not in en_ddragon_map:
            for k, v in en_ddragon_map.items():
                if int(v['key']) == riot_id:
                    dd_alias = k
                    break

        en_dd = en_ddragon_map.get(dd_alias, {})
        ko_dd = ko_ddragon_map.get(dd_alias, {})

        cd_detail, cd_detail_ko = details_map.get(riot_id, ({}, {}))

        raw_details[alias] = {
            'cdragon_en': cd_detail,
            'cdragon_ko': cd_detail_ko,
            'ddragon_en': en_dd,
            'ddragon_ko': ko_dd
        }

        eng_name = en_dd.get('name', cd_champ.get('name', alias))
        ko_name = ko_dd.get('name', cd_detail_ko.get('name', eng_name))
        eng_title = en_dd.get('title', cd_detail.get('title', ''))
        ko_title = ko_dd.get('title', cd_detail_ko.get('title', ''))

        meta = CHAMPION_METADATA.get(alias, {'gender': 'Other', 'species': 'Human', 'region': 'Runeterra'})
        gender = meta['gender']
        species = meta['species']
        region = meta['region']

        tactical = cd_detail.get('tacticalInfo', {})
        attack_type = tactical.get('attackType', '')
        if not attack_type:
            range_val = en_dd.get('stats', {}).get('attackrange', 0)
            attack_type = 'ranged' if range_val > 300 else 'melee'

        tags = en_dd.get('tags', cd_champ.get('roles', []))
        tag_1 = tags[0] if len(tags) > 0 else ''
        tag_2 = tags[1] if len(tags) > 1 else ''

        partype = en_dd.get('partype', '')
        if not partype or partype == '':
            partype = 'None'

        stats = en_dd.get('stats', {})

        hp_base = stats.get('hp', 0)
        hp_per = stats.get('hpperlevel', 0)
        hp_max = round(hp_base + (hp_per * 17), 2)

        mp_base = stats.get('mp', 0)
        mp_per = stats.get('mpperlevel', 0)
        mp_max = round(mp_base + (mp_per * 17), 2)
        # Note: Original Riot json had Viego mp_base and mp_max set to 10000. Set to 0 to avoid outlier distortion.
        if alias == 'Viego':
            mp_base = 0
            mp_max = 0

        movespeed = stats.get('movespeed', 0)

        armor_base = stats.get('armor', 0)
        armor_per = stats.get('armorperlevel', 0)
        armor_max = round(armor_base + (armor_per * 17), 2)

        spellblock_base = stats.get('spellblock', 0)
        spellblock_per = stats.get('spellblockperlevel', 0)
        spellblock_max = round(spellblock_base + (spellblock_per * 17), 2)

        attackrange = stats.get('attackrange', 0)

        hpregen_base = stats.get('hpregen', 0)
        hpregen_per = stats.get('hpregenperlevel', 0)
        hpregen_max = round(hpregen_base + (hpregen_per * 17), 2)

        mpregen_base = stats.get('mpregen', 0)
        mpregen_per = stats.get('mpregenperlevel', 0)
        mpregen_max = round(mpregen_base + (mpregen_per * 17), 2)

        crit_base = stats.get('crit', 0)
        crit_per = stats.get('critperlevel', 0)
        crit_max = round(crit_base + (crit_per * 17), 2)

        ad_base = stats.get('attackdamage', 0)
        ad_per = stats.get('attackdamageperlevel', 0)
        ad_max = round(ad_base + (ad_per * 17), 2)

        as_base = stats.get('attackspeed', 0)
        as_per = stats.get('attackspeedperlevel', 0)
        as_max = round(as_base * (1 + (as_per * 17 / 100)), 4) if as_base else 0

        image_path = f"{order_idx}.png"
        image_name = en_dd.get('image', {}).get('full', f"{dd_alias}.png")
        image_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/img/champion/{image_name}"
        local_image_path = os.path.join(image_dir, image_path)
        download_file(image_url, local_image_path)

        champions_csv.append({
            'champion_id': order_idx,
            'riot_id': riot_id,
            'alias': alias,
            'name_en': eng_name,
            'name_ko': ko_name,
            'title_en': eng_title,
            'title_ko': ko_title,
            'gender': gender,
            'species': species,
            'region': region,
            'attack_type': attack_type,
            'tag_1': tag_1,
            'tag_2': tag_2,
            'partype': partype,
            'hp_base': hp_base,
            'hp_max': hp_max,
            'mp_base': mp_base,
            'mp_max': mp_max,
            'movespeed': movespeed,
            'armor_base': armor_base,
            'armor_max': armor_max,
            'spellblock_base': spellblock_base,
            'spellblock_max': spellblock_max,
            'attackrange': attackrange,
            'hpregen_base': hpregen_base,
            'hpregen_max': hpregen_max,
            'mpregen_base': mpregen_base,
            'mpregen_max': mpregen_max,
            'crit_base': crit_base,
            'crit_max': crit_max,
            'attackdamage_base': ad_base,
            'attackdamage_max': ad_max,
            'attackspeed_base': as_base,
            'attackspeed_max': as_max,
            'image_path': image_path
        })

        name_map_csv.append({
            'champion_id': order_idx,
            'english_name': eng_name,
            'local_name': ko_name
        })

    print("Writing all_champions_detail_raw.json...")
    with open(os.path.join(raw_dir, 'all_champions_detail_raw.json'), 'w', encoding='utf-8') as f:
        json.dump(raw_details, f, ensure_ascii=False, indent=2)

    champions_filepath = os.path.join(data_dir, 'champions.csv')
    with open(champions_filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=champions_csv[0].keys())
        writer.writeheader()
        writer.writerows(champions_csv)
    print(f"Saved {champions_filepath}")

    name_map_filepath = os.path.join(data_dir, 'name_map.csv')
    with open(name_map_filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['champion_id', 'english_name', 'local_name'])
        writer.writeheader()
        writer.writerows(name_map_csv)
    print(f"Saved {name_map_filepath}")

if __name__ == '__main__':
    main()
