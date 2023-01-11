from argparse import ArgumentParser, Namespace
from logging import getLogger

from pinyin_to_ipa import pinyin_to_ipa
from pinyin_to_ipa_cli.argparse_helper import parse_non_empty_or_whitespace


def get_app_try_add_vocabulary_from_pronunciations_parser(parser: ArgumentParser):
  parser.description = "Command-line interface (CLI) to transcribe pinyin to IPA."
  parser.add_argument("pinyin", metavar='PINYIN', type=parse_non_empty_or_whitespace,
                      help="pinyin")
  parser.add_argument("--sep", type=str, help="separator between phonemes", default="")
  parser.add_argument("--first", action="store_true", help="return only first result")
  return get_pronunciations_files


def get_pronunciations_files(ns: Namespace) -> bool:
  logger = getLogger(__name__)

  try:
    result = pinyin_to_ipa(ns.pinyin)
  except ValueError as error:
    logger.info("No IPA transcription available!")
    logger.debug(error)
    return False

  assert len(result) > 0

  if ns.first:
    print(ns.sep.join(result[0]))
  else:
    for res in result:
      print(ns.sep.join(res))
  return True
