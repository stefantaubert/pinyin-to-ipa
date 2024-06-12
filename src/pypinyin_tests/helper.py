from pathlib import Path
from typing import Set


def get_most_pinyin_syllables_toneless() -> Set[str]:
  voc = Path("res/most-syllables-toneless.txt").read_text("UTF-8")
  syllables = set(voc.splitlines())
  return syllables


def get_possible_pinyin_syllables_tone3() -> Set[str]:
  voc = Path("res/possible-syllables-tone3.txt").read_text("UTF-8")
  syllables = set(voc.splitlines())
  return syllables
