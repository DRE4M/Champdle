interface Champion {
  champion_id: number
  riot_id: number
  alias: string
  name_en: string
  name_ko: string
  title_en: string
  title_ko: string
  gender: string
  species: string
  region: string
  attack_type: string
  tag_1: string
  tag_2?: string
  partype: string
  hp_base: number
  hp_max: number
  mp_base: number
  mp_max: number
  movespeed: number
  armor_base: number
  armor_max: number
  spellblock_base: number
  spellblock_max: number
  attackrange: number
  hpregen_base: number
  hpregen_max: number
  mpregen_base: number
  mpregen_max: number
  crit_base: number
  crit_max: number
  attackdamage_base: number
  attackdamage_max: number
  attackspeed_base: number
  attackspeed_max: number
  image_path?: string
}

interface LocalName {
  english_name: string
  local_name: string
}

interface GuessResult {
  name: string
  rank: number
  similarity: number
}

interface GuessData {
  index: number
  name: string
  rank: number
  similarity: number
}

interface State {
  puzzle_number: number
  guess_data_list: GuessData[]
  last_guess_data: GuessData | undefined
  locale: string | undefined
  api_data: ApiData
  statistics: Statistics
}

interface ApiData {
  champions: Champion[]
  champion_local_name_map: Record<string, string>
  champion_english_name_map: Record<string, string>
}

interface Statistics {
  last_puzzle_number: number
  clear_count: number
  last_guess_count: number
  total_guess_count: number
  streak: number
  best_streak: number
  last_correct_guess: undefined | GuessData
  last_best_guess: undefined | GuessData
}
