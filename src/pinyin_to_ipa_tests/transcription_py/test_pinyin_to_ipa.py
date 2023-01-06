
from pathlib import Path

from ordered_set import OrderedSet

from pinyin_to_ipa.transcription import pinyin_to_ipa


def test_ju():
  result = pinyin_to_ipa("ju")
  assert result == OrderedSet([('p', 'ə', 'ŋ')])


def test_beng():
  result = pinyin_to_ipa("beng")
  assert result == OrderedSet([('p', 'ə', 'ŋ')])


def test_n():
  result = pinyin_to_ipa("ń")
  assert result == "n"


def test_voc():
  voc = Path("res/most-syllables.txt").read_text("UTF-8")
  syllables = voc.splitlines()
  result = []
  for syllable in syllables:
    res = pinyin_to_ipa(syllable)
    result.append((syllable, res))
  assert len(result) == len(syllables)
