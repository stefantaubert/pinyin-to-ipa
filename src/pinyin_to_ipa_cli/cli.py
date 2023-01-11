import argparse
import logging
import sys
from argparse import ArgumentParser
from importlib.metadata import version
from logging import getLogger
from typing import Callable, Generator, List, Tuple

from pinyin_to_ipa_cli.main import get_app_try_add_vocabulary_from_pronunciations_parser

__version__ = version("pinyin-to-ipa")

INVOKE_HANDLER_VAR = "invoke_handler"


Parsers = Generator[Tuple[str, str, Callable], None, None]


def formatter(prog):
  return argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=40)


def _init_parser():
  main_parser = ArgumentParser(formatter_class=formatter)
  main_parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
  method = get_app_try_add_vocabulary_from_pronunciations_parser(main_parser)
  main_parser.set_defaults(**{
      INVOKE_HANDLER_VAR: method,
  })

  return main_parser


def configure_logger(productive: bool) -> None:
  loglevel = logging.INFO if productive else logging.DEBUG
  main_logger = getLogger()
  main_logger.setLevel(loglevel)
  main_logger.manager.disable = logging.NOTSET
  if len(main_logger.handlers) > 0:
    console = main_logger.handlers[0]
  else:
    console = logging.StreamHandler()
    main_logger.addHandler(console)

  logging_formatter = logging.Formatter(
    '%(message)s',
    '%Y/%m/%d %H:%M:%S',
  )
  console.setFormatter(logging_formatter)
  console.setLevel(loglevel)


def parse_args(args: List[str], productive: bool = False):
  configure_logger(productive)
  logger = getLogger(__name__)
  logger.debug("Received args:")
  logger.debug(args)
  parser = _init_parser()
  if len(args) == 0:
    parser.print_help()
    sys.exit(0)

  try:
    received_args = parser.parse_args(args)
  except SystemExit as error:
    error_code = error.args[0]
    # -v -> 0; invalid arg -> 2
    sys.exit(error_code)

  params = vars(received_args)

  if INVOKE_HANDLER_VAR in params:
    invoke_handler: Callable[[ArgumentParser], None] = params.pop(INVOKE_HANDLER_VAR)
    success = invoke_handler(received_args)
    if success:
      sys.exit(0)
    sys.exit(1)
  else:
    parser.print_help()


def run(productive: bool):
  arguments = sys.argv[1:]
  parse_args(arguments, productive)


def run_prod():
  run(True)


if __name__ == "__main__":
  run(not __debug__)
