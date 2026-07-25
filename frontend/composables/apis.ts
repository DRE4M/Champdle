export const apiLanguages = () =>
  $fetch<Array<string>>(`${apiBase()}/languages`)

export const apiChampions = () => $fetch<Array<Champion>>(`${apiBase()}/champions`)

export const apiChampionNameMap = (language: string) =>
  $fetch<Array<LocalName>>(`${apiBase()}/champion_name_map/${language}`)

export const apiRank = (puzzle_number: number) =>
  $fetch<Array<GuessResult>>(`${apiBase()}/rank/${puzzle_number}`)

export const apiGuess = (puzzle_number: number, name: string) =>
  $fetch<GuessResult>(`${apiBase()}/guess/${puzzle_number}?name=${encodeURIComponent(name)}`)
