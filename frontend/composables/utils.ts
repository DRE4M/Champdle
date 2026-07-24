import parser from "accept-language-parser"
import { Buffer } from "buffer"

export const puzzleOriginDate = new Date("2022-04-28T00:00:00")

export const dateToPuzzleNumber = (dateStr: string): number => {
  const target = new Date(dateStr)
  if (isNaN(target.getTime())) return todayPuzzleNumber()
  return Math.floor((target.getTime() - puzzleOriginDate.getTime()) / 86400000)
}

export const puzzleNumberToDateString = (puzzleNum: number): string => {
  const date = new Date(puzzleOriginDate.getTime() + puzzleNum * 86400000)
  return date.toISOString().split("T")[0]
}

export const todayPuzzleNumber = () => {
  if (process.client) {
    const urlParams = new URLSearchParams(window.location.search)
    const puzzleParam = urlParams.get("puzzle")
    if (puzzleParam && !isNaN(parseInt(puzzleParam))) {
      return parseInt(puzzleParam)
    }
    const dateParam = urlParams.get("date")
    if (dateParam) {
      const target = new Date(dateParam)
      if (!isNaN(target.getTime())) {
        return Math.floor((target.getTime() - puzzleOriginDate.getTime()) / 86400000)
      }
    }
  }
  const today = new Date()
  const days = Math.floor((today.getTime() - puzzleOriginDate.getTime()) / 86400000)
  return days
}

export const getLocale = (): string => {
  let lang: string
  if (process.client) {
    if (window.navigator.languages && window.navigator.languages.length) {
      lang = window.navigator.languages[0].split("-")[0]
    } else {
      lang =
        window.navigator.userLanguage ||
        window.navigator.language ||
        window.navigator.browserLanguage ||
        "en"
    }
  } else {
    const accept_language: string | undefined = useRequestHeaders([
      "accept-language",
    ])["accept-language"]
    if (accept_language !== undefined) {
      lang = parser.pick(Object.keys(fluentBundles), accept_language, {
        loose: true,
      })
    } else {
      lang = "en"
    }
  }
  return lang.split("-")[0]
}

export const utf8ToB64 = (str: string): string => {
  return Buffer.from(str, "utf8").toString("base64")
}

export const b64ToUtf8 = (str: string): string => {
  return Buffer.from(str, "base64").toString("utf8")
}

export const apiBase = (): string => {
  return process.client ? api_client_base.value : api_server_base.value
}

export const missingChampionImageUrl = (): string => {
  return "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'><rect width='100%' height='100%' fill='%23334155'/><text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' font-size='40' fill='%2394a3b8'>?</text></svg>"
}

export const fallbackChampionImageUrl = (imagePath?: string): string => {
  return missingChampionImageUrl()
}

export const missingPokemonImageUrl = missingChampionImageUrl
export const fallbackPokemonImageUrl = fallbackChampionImageUrl
