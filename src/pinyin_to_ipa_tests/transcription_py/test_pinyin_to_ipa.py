
from pathlib import Path

from ordered_set import OrderedSet
from pytest import raises

from pinyin_to_ipa.transcription import pinyin_to_ipa

# PINYIN without finals: hm, hng, m̀, m̄, n, ng, ń, ńg, ň, ňg, ǹ, ǹg, ḿ


def test_empty():
  with raises(ValueError) as error:
    pinyin_to_ipa("")


def test_whitespace():
  with raises(ValueError) as error:
    pinyin_to_ipa(" ")


def test_non_pinyin_a__raises_value_error():
  with raises(ValueError) as error:
    pinyin_to_ipa("?abc")
  assert error.value.args[0] == "Parameter 'pinyin': Tone 'c' couldn't be detected!"


def test_non_pinyin__raises_value_error():
  with raises(ValueError) as error:
    pinyin_to_ipa("test")


def test_pinyin_syllabic_consonant_hng__tone5():
  result = pinyin_to_ipa("hng")
  assert result == OrderedSet([('h', 'ŋ',)])


def test_pinyin_syllabic_consonant_ng__tone3():
  result = pinyin_to_ipa("ňg")
  assert result == OrderedSet([('ŋ˧˩˧',)])


def test_pinyin_syllabic_consonant_ng__tone5():
  result = pinyin_to_ipa("ng")
  assert result == OrderedSet([('ŋ',)])


def test_pinyin_syllabic_consonant_n__tone2():
  result = pinyin_to_ipa("ń")
  assert result == OrderedSet([('n˧˥',)])


def test_pinyin_syllabic_consonant_n__tone3():
  result = pinyin_to_ipa("ň")
  assert result == OrderedSet([('n˧˩˧',)])


def test_pinyin_syllabic_consonant_n__tone4():
  result = pinyin_to_ipa("ǹ")
  assert result == OrderedSet([('n˥˩',)])


def test_pinyin_syllabic_consonant_n__tone5():
  result = pinyin_to_ipa("n")
  assert result == OrderedSet([('n',)])


def test_pinyin_without_initial_tone1():
  result = pinyin_to_ipa("yuē")
  assert result == OrderedSet([('ɥ', 'e˥')])


def test_pinyin_without_initial_tone2():
  result = pinyin_to_ipa("yué")
  assert result == OrderedSet([('ɥ', 'e˧˥')])


def test_pinyin_without_initial_tone3():
  result = pinyin_to_ipa("yuě")
  assert result == OrderedSet([('ɥ', 'e˧˩˧')])


def test_pinyin_without_initial_tone4():
  result = pinyin_to_ipa("yuè")
  assert result == OrderedSet([('ɥ', 'e˥˩')])


def test_pinyin_without_initial_tone5():
  result = pinyin_to_ipa("yue")
  assert result == OrderedSet([('ɥ', 'e')])


def test_beng():
  result = pinyin_to_ipa("beng")
  assert result == OrderedSet([('p', 'ə', 'ŋ')])


def test_an():
  result = pinyin_to_ipa("an")
  assert result == OrderedSet([('a', 'n')])


def test_ang():
  result = pinyin_to_ipa("ang")
  assert result == OrderedSet([('a', 'ŋ')])


def test_fěi():
  result = pinyin_to_ipa("fěi")
  assert result == OrderedSet([('f', 'ei̯˧˩˧')])


def test_voc():
  voc = Path("res/most-syllables.txt").read_text("UTF-8")
  syllables = voc.splitlines()
  result = []
  for syllable in syllables:
    res = pinyin_to_ipa(syllable)
    result.append((syllable, res))
  assert len(result) == len(syllables)


def test_syllables_toneless__raise_no_error():
  voc = Path("res/most-syllables-toneless.txt").read_text("UTF-8")
  syllables = voc.splitlines()
  result = []
  failed = OrderedSet()
  for syllable in syllables:
    try:
      res = pinyin_to_ipa(syllable)
    except ValueError as error:
      failed.add(syllable)
    result.append((syllable, res))
  assert len(result) == len(syllables)


def test_possible_syllables__raise_no_error():
  voc = Path("res/possible-syllables-tone3.txt").read_text("UTF-8")
  syllables = voc.splitlines()
  result = []
  failed = OrderedSet()
  for syllable in syllables:
    try:
      res = pinyin_to_ipa(syllable)
    except ValueError as error:
      failed.add(syllable)
    result.append((syllable, res))
  assert len(result) == len(syllables)
