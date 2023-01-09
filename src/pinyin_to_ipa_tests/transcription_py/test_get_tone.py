
from pathlib import Path

from ordered_set import OrderedSet
from pytest import raises

from pinyin_to_ipa.transcription import get_tone


def test_empty__raises_value_error():
  with raises(ValueError) as error:
    get_tone("")
  assert error.value.args[0] == "Parameter 'pinyin': Tone couldn't be detected!"


def test_whitespace__returns_5():
  result = get_tone(" ")
  assert result == 5


def test_non_pinyin_with_question_mark__raises_value_error():
  with raises(ValueError) as error:
    get_tone("?abc")
  assert error.value.args[0] == "Parameter 'pinyin': Tone 'c' couldn't be detected!"


def test_invalid_pinyin__lün__raises_value_error():
  with raises(ValueError) as error:
    get_tone("lün")
  assert error.value.args[0] == "Parameter 'pinyin': Tone 'n' couldn't be detected!"


def test_non_pinyin__returns_5():
  result = get_tone("test")
  assert result == 5
