from collections import Counter

from ordered_set import OrderedSet
from pypinyin.contrib.tone_convert import to_finals, to_normal
from pypinyin.style._constants import _FINALS

from pypinyin_tests.helper import (
  get_most_pinyin_syllables_toneless,
  get_possible_pinyin_syllables_tone3,
)

COMMON_FINALS = {
  "a",
  "ai",
  "an",
  "ang",
  "ao",
  "e",
  "ei",
  "en",
  "eng",
  "er",
  "i",
  "ia",
  "ian",
  "iang",
  "iao",
  "ie",
  "in",
  "ing",
  "iong",
  "o",
  "ong",
  "ou",
  "u",
  "ua",
  "uai",
  "uan",
  "uang",
  "uo",
  "ê",
  "ü",
  "üe",
  "ün",
}


def test_get_finals_strict_returns_all_finals() -> None:
  failed = OrderedSet()
  finials = []
  syllables = (
    get_most_pinyin_syllables_toneless() | get_possible_pinyin_syllables_tone3()
  )
  for syllable in syllables:
    try:
      pinyin_normal = to_normal(syllable, v_to_u=True)
      f = to_finals(pinyin_normal, strict=True, v_to_u=True)
      finials.append(f)
    except ValueError:  # noqa: PERF203
      failed.add(syllable)
  finals_count = Counter(finials)
  result = set(finals_count.keys())
  assert len(failed) == 0
  strict_finals = COMMON_FINALS | {"", "iou", "uei", "uen", "ueng", "üan"}
  assert result == strict_finals
  assert result == set(_FINALS) | {""}


def test_get_finals_non_strict_returns_all_finals() -> None:
  failed = OrderedSet()
  finials = []
  syllables = (
    get_most_pinyin_syllables_toneless() | get_possible_pinyin_syllables_tone3()
  )
  for syllable in syllables:
    try:
      pinyin_normal = to_normal(syllable, v_to_u=True)
      f = to_finals(pinyin_normal, strict=False, v_to_u=True)
      finials.append(f)
    except ValueError:  # noqa: PERF203
      failed.add(syllable)
  finals_count = Counter(finials)
  result = set(finals_count.keys())
  assert len(failed) == 0
  non_strict_finals = COMMON_FINALS | {"g", "iu", "m", "n", "ng", "ue", "ui", "un"}
  assert result == non_strict_finals
