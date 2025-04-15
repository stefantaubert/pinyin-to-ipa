from collections import Counter

from ordered_set import OrderedSet
from pypinyin.contrib.tone_convert import to_initials, to_normal
from pypinyin.style._constants import _INITIALS, _INITIALS_NOT_STRICT

from pypinyin_tests.helper import (
  get_most_pinyin_syllables_toneless,
  get_possible_pinyin_syllables_tone3,
)

COMMON_INITIALS = {
  "",
  "b",
  "c",
  "ch",
  "d",
  "f",
  "g",
  "h",
  "j",
  "k",
  "l",
  "m",
  "n",
  "p",
  "q",
  "r",
  "s",
  "sh",
  "t",
  "x",
  "z",
  "zh",
}


def test_get_initials_strict_returns_all_initials():
  failed = OrderedSet()
  initials = []
  syllables = (
    get_most_pinyin_syllables_toneless() | get_possible_pinyin_syllables_tone3()
  )
  for syllable in syllables:
    try:
      pinyin_normal = to_normal(syllable, v_to_u=True)
      i = to_initials(pinyin_normal, strict=True)
      initials.append(i)
    except ValueError:
      failed.add(syllable)
  initials_count = Counter(initials)
  result = set(initials_count.keys())
  assert len(failed) == 0
  assert result == COMMON_INITIALS
  assert result == set(_INITIALS) | {""}


def test_get_initials_non_strict_returns_all_initials():
  failed = OrderedSet()
  initials = []
  syllables = (
    get_most_pinyin_syllables_toneless() | get_possible_pinyin_syllables_tone3()
  )
  for syllable in syllables:
    try:
      pinyin_normal = to_normal(syllable, v_to_u=True)
      i = to_initials(pinyin_normal, strict=False)
      initials.append(i)
    except ValueError:
      failed.add(syllable)
  initials_count = Counter(initials)
  result = set(initials_count.keys())
  assert len(failed) == 0
  assert result == COMMON_INITIALS | {"w", "y"}
  assert result == set(_INITIALS_NOT_STRICT) | {""}
