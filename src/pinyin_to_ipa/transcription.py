import itertools
from typing import Tuple

from ordered_set import OrderedSet
from pypinyin.contrib.tone_convert import to_finals, to_initials, to_normal

# References
# https://en.wikipedia.org/wiki/Help:IPA/Mandarin
# https://en.wikipedia.org/wiki/Standard_Chinese_phonology
# https://en.wikipedia.org/wiki/Pinyin
# https://de.wikipedia.org/wiki/Pinyin

INITIAL_MAPPING = {
  "b": [("p",)],
  "c": [("tsʰ",)],
  "ch": [("ʈʂʰ",)],
  "d": [("t",)],
  "f": [("f",)],
  "g": [("k",)],
  "h": [("x",), ("h",)],
  "j": [("tɕ",)],
  "k": [("kʰ",)],
  "l": [("l",)],
  "m": [("m",)],
  "n": [("n",)],
  "p": [("pʰ",)],
  "q": [("tɕʰ",)],
  "r": [("ʐ",), ("ɻ",)],
  "s": [("s",)],
  "sh": [("ʂ",)],
  "t": [("tʰ",)],
  "x": [("ɕ",)],
  "z": [("ts",)],
  "zh": [("ʈʂ",)],
  "w": [("w",)],
  "y": [("j",), ("ɥ",)],
}

# Duanmu (2000, p. 37) and Lin (2007)
FINAL_MAPPING = {
  "a": [("a",)],
  "ai": [("ai̯",)],
  "an": [("a", "n")],
  "ang": [("a", "ŋ")],
  "ao": [("au̯",)],
  "e": [("ɤ",)],
  "ei": [("ei̯")],
  "en": [("ə", "n")],
  "eng": [("ə", "ŋ")],
  # Note: In a small number of independent words or morphemes pronounced [ɚ] or [aɚ̯], written in pinyin as er (with some tone), such as 二 èr "two", 耳 ěr "ear", and 儿 (traditional 兒) ér "son". Similar to the sound in bar in English. Can also be pronounced [ɚ] depending on the speaker.
  "er": [("ɚ",), ("aɚ̯",)],
  "i": [("i",)],
  "ia": [("j", "a")],
  "ian": [("j", "ɛ", "n")],
  "iang": [("j", "a", "ŋ")],
  "iao": [("j", "au̯")],
  "ie": [("j", "e")],
  "in": [("i", "n")],
  "iu": [("j", "ou̯")],
  "iou": [("j", "ou̯")],
  "ing": [("i", "ŋ")],
  "iong": [("j", "ʊ", "ŋ")],
  "io": [("j", "ɔ")],  # interjection
  "o": [("ɔ",)],  # interjection
  "ong": [("ʊ", "ŋ")],
  "ou": [("ou̯",)],
  "u": [("u",)],
  "ui": [("w", "ei̯")],
  "uei": [("w", "ei̯")],
  "ua": [("w", "a")],
  "uai": [("w", "ai̯")],
  "uan": [("w", "a", "n")],
  "un": [("w", "ə", "n")],
  "uen": [("w", "ə", "n")],
  "uang": [("w", "a", "ŋ")],
  "ueng": [("w", "ə", "ŋ")],
  "uo": [("w", "o")],
  "ü": [("y",)],
  "v": [("y",)],
  "üe": [("ɥ", "e")],
  "ve": [("ɥ", "e")],
  "üan": [("ɥ", "ɛ", "n")],
  "van": [("ɥ", "ɛ", "n")],
  "ün": [("y", "n")],
  "vn": [("y", "n")],
  "ê": [("ɛ",)],  # interjection
}

# Note: [ɻ̩ ~ ʐ̩], an apical retroflex voiced continuant,[a] in zhi, chi, shi, ri ([ʈʂɻ̩ ʈʂʰɻ̩ ʂɻ̩ ɻɻ̩]).
FINAL_MAPPING_AFTER_ZH_CH_SH_R = {
  "i": [("ɻ̩",)],
}

# Note: [ɹ̩ ~ z̩], a laminal denti-alveolar voiced continuant,[a] in zi, ci, si ([tsɹ̩ tsʰɹ̩ sɹ̩]);
FINAL_MAPPING_AFTER_Z_C_S = {
  "i": [("ɹ̩",)],
}

# Note: ü is written as u after j, q, or x (the /u/ phoneme never occurs in these positions)
FINAL_MAPPING_AFTER_J_Q_X = {
  "u": FINAL_MAPPING["ü"],
  "ue": FINAL_MAPPING["üe"],
  "uan": FINAL_MAPPING["üan"],
  "un": FINAL_MAPPING["ün"],
}

# Note: uo is written as o after b, p, m, or f.
FINAL_MAPPING_AFTER_B_P_M_F = {
  "o": FINAL_MAPPING["ou"]
}


def pinyin_to_ipa(pinyin: str) -> Tuple[str, ...]:
  parts = []
  pinyin = to_normal(pinyin)
  pinyin_initial = to_initials(pinyin)
  if pinyin_initial != "":
    assert pinyin_initial in INITIAL_MAPPING
    initial_phoneme = INITIAL_MAPPING[pinyin_initial]
    parts.append(initial_phoneme)

  pinyin_final = to_finals(pinyin)
  if pinyin_final != "":
    final_phonemes = None
    if pinyin_initial in {"zh", "ch", "sh", "r"} and pinyin_final in FINAL_MAPPING_AFTER_ZH_CH_SH_R:
      final_phonemes = FINAL_MAPPING_AFTER_ZH_CH_SH_R[pinyin_final]
    elif pinyin_initial in {"j", "q", "x"} and pinyin_final in FINAL_MAPPING_AFTER_J_Q_X:
      final_phonemes = FINAL_MAPPING_AFTER_J_Q_X[pinyin_final]
    elif pinyin_initial in {"b", "p", "m", "f"} and pinyin_final in FINAL_MAPPING_AFTER_B_P_M_F:
      final_phonemes = FINAL_MAPPING_AFTER_B_P_M_F[pinyin_final]
    else:
      assert pinyin_final in FINAL_MAPPING
      final_phonemes = FINAL_MAPPING[pinyin_final]

    parts.append(final_phonemes)

  assert len(parts) > 0

  all_syllable_combinations = OrderedSet(
    tuple(itertools.chain.from_iterable(combination))
    for combination in itertools.product(*parts)
  )

  return all_syllable_combinations
