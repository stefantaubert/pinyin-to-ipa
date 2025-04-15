from pypinyin.style._constants import _FINALS

from pinyin_to_ipa.transcription import FINAL_MAPPING


def test_mapping_contain_all_finals() -> None:
  missing_finals = set(_FINALS) - FINAL_MAPPING.keys()
  additional_finals = FINAL_MAPPING.keys() - set(_FINALS)
  missing_finals_that_are_expected = {"er", "ê"}
  assert missing_finals == missing_finals_that_are_expected
  assert len(additional_finals) == 0
