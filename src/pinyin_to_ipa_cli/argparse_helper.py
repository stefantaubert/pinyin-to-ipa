from argparse import ArgumentTypeError
from typing import Optional


def parse_non_empty_or_whitespace(value: str) -> str:
  value = parse_required(value)
  if value.strip() == "":
    raise ArgumentTypeError("Value must not be empty or whitespace!")
  return value


def parse_required(value: Optional[str]) -> str:
  if value is None:
    raise ArgumentTypeError("Value must not be None!")
  return value
