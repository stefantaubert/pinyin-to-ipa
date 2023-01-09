from argparse import ArgumentParser, Namespace
from collections import OrderedDict
from functools import partial
from logging import getLogger
from multiprocessing.pool import Pool
from pathlib import Path
from tempfile import gettempdir
from typing import Dict, Optional, Tuple

from ordered_set import OrderedSet

from pinyin_to_ipa import pinyin_to_ipa
from pinyin_to_ipa_cli.argparse_helper import (DEFAULT_PUNCTUATION, ConvertToOrderedSetAction,
                                               add_chunksize_argument, add_encoding_argument,
                                               add_maxtaskperchild_argument, add_n_jobs_argument,
                                               add_serialization_group, get_optional,
                                               parse_existing_file, parse_non_empty_or_whitespace,
                                               parse_path, parse_positive_float)


def get_app_try_add_vocabulary_from_pronunciations_parser(parser: ArgumentParser):
  parser.description = "Command-line interface (CLI) to create a pronunciation dictionary by looking up IPA transcriptions using dragonmapper including the possibility of ignoring punctuation and splitting words on hyphens before transcribing them."
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
