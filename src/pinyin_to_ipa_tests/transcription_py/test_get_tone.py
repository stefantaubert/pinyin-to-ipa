from pytest import raises

from pinyin_to_ipa.transcription import get_tone


def test_empty__raises_value_error() -> None:
  with raises(ValueError) as error:
    get_tone("")
  assert error.value.args[0] == "Parameter 'pinyin': Tone couldn't be detected!"


def test_whitespace__returns_5() -> None:
  result = get_tone(" ")
  assert result == 5


def test_non_pinyin_with_question_mark__raises_value_error() -> None:
  with raises(ValueError) as error:
    get_tone("?abc")
  assert error.value.args[0] == "Parameter 'pinyin': Tone 'c' couldn't be detected!"


def test_previously_buggy_pinyin__lün5__raises_value_error__is_fail() -> None:
  # before v0.50 this resulted in an error
  tone = get_tone("lün")
  assert tone == 5


def test_previously_buggy_pinyin__lün2__raises_value_error__is_fail() -> None:
  # before v0.50 this resulted in an error
  tone = get_tone("lǘn")  # tone 2
  assert tone == 2


def test_previously_buggy_pinyin__lün3__raises_value_error__is_fail() -> None:
  # before v0.50 this resulted in an error
  tone = get_tone("lün3")
  assert tone == 3


def test_non_pinyin__returns_5() -> None:
  result = get_tone("test")
  assert result == 5
