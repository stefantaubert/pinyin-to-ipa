from pypinyin.style._constants import _FINALS

from pinyin_to_ipa.transcription import FINAL_MAPPING


def test_contain_only_all_finals():
  missing_finals = set(_FINALS) - FINAL_MAPPING.keys()
  additional_finals = FINAL_MAPPING.keys() - set(_FINALS)
  assert missing_finals == {'er', 'ê'}
  assert len(additional_finals) == 0
