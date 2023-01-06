import string

STRESS_PRIMARY = "\u02C8"  # ˈ
STRESS_SECONDARY = "\u02CC"  # ˌ

LONG = "\u02D0"  # ː
HALF_LONG = "\u02D1"  # eˑ
EXTRA_SHORT = "\u0306"  # ə̆
NASAL = "\u0303"  # ẽ ɾ̃
RAISED = "\u031D"  # r̝
TIE_ABOVE = "\u0361"  # ͡
TIE_BELOW = "\u035C"  # ͜

SYLLABIC = "\u0329"  # n̩
NON_SYLLABIC = "\u032F"

BREAK_SYLLABLE = "."
BREAK_MINOR = "|"
BREAK_MAJOR = "\u2016"  # ‖
BREAK_WORD = "#"

INTONATION_RISING = "\u2197"  # ↗
INTONATION_FALLING = "\u2198"  # ↘

TONE_1 = "¹"
TONE_2 = "²"
TONE_3 = "³"
TONE_4 = "⁴"
TONE_5 = "⁵"
TONE_6 = "⁶"
TONE_7 = "⁷"
TONE_8 = "⁸"
TONE_9 = "⁹"

TONE_EXTRA_HIGH = "˥"
TONE_HIGH = "˦"
TONE_MID = "˧"
TONE_LOW = "˨"
TONE_EXTRA_LOW = "˩"

TONE_EXTRA_HIGH_ALT = "\u030B"
TONE_HIGH_ALT = "\u0301"
TONE_MID_ALT = "\u0304"
TONE_LOW_ALT = "\u0300"
TONE_EXTRA_LOW_ALT = "\u030F"

TONES = {
  TONE_1,
  TONE_2,
  TONE_3,
  TONE_4,
  TONE_5,
  TONE_6,
  TONE_7,
  TONE_8,
  TONE_9,
  TONE_EXTRA_HIGH,
  TONE_EXTRA_HIGH,
  TONE_HIGH,
  TONE_MID,
  TONE_LOW,
  TONE_EXTRA_LOW,
  TONE_EXTRA_HIGH_ALT,
  TONE_EXTRA_HIGH_ALT,
  TONE_HIGH_ALT,
  TONE_MID_ALT,
  TONE_LOW_ALT,
  TONE_EXTRA_LOW_ALT,
}

TONE_GLOTTALIZED = "ˀ"

ASPIRATED = "\u02B0"  # ʰ
BREATHY_VOICE_ASPIRATED = "\u02B1"  # ʱ

BRACKET_PHONETIC_LEFT = "["
BRACKET_PHONETIC_RIGHT = "]"
BRACKET_PHONEMIC_LEFT = "/"
BRACKET_PHONEMIC_RIGHT = "/"
BRACKET_PROSODIC_LEFT = "{"
BRACKET_PROSODIC_RIGHT = "}"
BRACKET_OPTIONAL_LEFT = "("
BRACKET_OPTIONAL_RIGHT = ")"

VOWELS = {
  "i",
  "y",
  "ɨ",
  "ᵻ",
  "ʉ",
  "ɯ",
  "u",
  "ɪ",
  "ʏ",
  "ʊ",
  "e",
  "ø",
  "ɘ",
  "ɵ",
  "ɤ",
  "o",
  "ɛ",
  "œ",
  "ɜ",
  "ɞ",
  "ʌ",
  "ɔ",
  "æ",
  "ɐ",
  "a",
  "ɶ",
  "ɑ",
  "ɒ",
}

SCHWAS = {
  "ə",
  "ɚ",
  "ɝ",
}

# TODO rename
ENG_ARPA_DIPHTONGS = {
  "aʊ",
  "aɪ",
  "eɪ",  # "engraved"
  "oʊ",  # "only"
  "ɔɪ",  # "boy", "avoidance"
}

ENG_DIPHTHONGS = ENG_ARPA_DIPHTONGS | {
  "æʊ",
  "æɔ",
  "æɪ",
  "ʌʊ",
  "ʌɪ",
  "oɪ",
  "ʉu",
  "iʌ",  # extra
  "ɪər",
  "ɪə",
  "ɪɹ",
  "ɛər",
  "ɛɪ",  # extra
  "ɛə",
  "eə",  # extra "air"
  "eər",  # extra
  "eʊ",  # extra "boat"
  "ɛɹ",
  "ʊər",
  "ʊə",
  "ʊu",
  "ʊɹ",
  # "ɝʌ",  # extra
  # "ɝi",  # extra
}

CONSONANTS = {
  "m",
  "ɱ",
  "n",
  "ɳ",
  "ɲ",
  "ŋ",
  "ɴ",
  "p",
  "b",
  "t",
  "d",
  "ʈ",
  "ɖ",
  "c",
  "ɟ",
  "k",
  "ɡ",
  "g",
  "q",
  "ɢ",
  "ʡ",
  "ʔ",
  "p͡f",
  "b͡v",
  "t̪͡s",
  "b͡v",
  "t͡s",
  "d͡z",
  "t͡ʃ",  # "Chinese"
  "d͡ʒ",
  "ʈ͡ʂ",
  "ɖ͡ʐ",
  "t͡ɕ",
  "d͡ʑ",
  "k͡x",
  "ɸ",
  "β",
  "f",
  "v",
  "θ",
  "ð",
  "s",
  "z",
  "ʃ",
  "ʒ",
  "ʂ",
  "ʐ",
  "ç",
  "ʐ",
  "x",
  "ɣ",
  "χ",
  "ʁ",
  "ħ",
  "h",
  "ɦ",
  "w",
  "ʍ",
  "ʋ",
  "ɹ",
  "ɻ",
  "j",
  "ɰ",
  "ⱱ",
  "ɾ",
  "ɽ",
  "ʙ",
  "r",
  "ʀ",
  "l",
  "ɫ",
  "ɭ",
  "ʎ",
  "ʟ",
}

CHARACTERS = VOWELS | SCHWAS | CONSONANTS

TIES = {
  TIE_ABOVE,
  TIE_BELOW,
}

APPENDIX = {
  LONG,
  HALF_LONG,
  EXTRA_SHORT,
  NASAL,
  RAISED,
  SYLLABIC,
  NON_SYLLABIC,
  TONE_GLOTTALIZED,
  ASPIRATED,
  BREATHY_VOICE_ASPIRATED,
} | TONES

STRESSES = {
  STRESS_PRIMARY,
  STRESS_SECONDARY,
}

PUNCTUATION_AND_WHITESPACE = set(string.punctuation) | set(string.whitespace)
