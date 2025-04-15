import pytest
from _pytest.monkeypatch import MonkeyPatch

from pinyin_to_ipa.transcription import get_initials


def test_zero_cons__yin__returns_none() -> None:
  result = get_initials("yin")
  assert result is None


def test_normal__xiong__returns_x() -> None:
  result = get_initials("xiong")
  assert result == "x"


def test_syllabic_consonant__hm__returns_none() -> None:
  result = get_initials("hm")
  assert result is None


def test_interjection__o__returns_none() -> None:
  result = get_initials("o")
  assert result is None


def test_invalid_pinyin__questionmarks__raises_no_value_error() -> None:
  result = get_initials("???")
  assert result is None


def test_invalid_pinyin__abc__raises_no_value_error() -> None:
  result = get_initials("abc")
  assert result is None


def test_buggy_pinyin__lün__raises_no_value_error() -> None:
  result = get_initials("lün")
  assert result == "l"


def test_invalid_pinyin__qqing__raises_no_value_error() -> None:
  result = get_initials("qqing")
  assert result == "q"


def test_get_initials__unexpected_return_from_to_initials__raises_value_error(
  monkeypatch: MonkeyPatch,
) -> None:
  def broken_to_initials(_: str, strict: bool = True) -> str:
    return "xyz"

  monkeypatch.setattr("pinyin_to_ipa.transcription.to_initials", broken_to_initials)

  with pytest.raises(ValueError, match="Initial 'xyz' couldn't be detected"):
    get_initials("ma")
