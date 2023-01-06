from typing import Optional, Set, Tuple

from pinyin_to_ipa.ipa_symbols import APPENDIX, PUNCTUATION_AND_WHITESPACE, STRESSES, TIES


def merge_fusion_with_ignore(symbols: Tuple[str, ...], fusion_symbols: Set[str], ignore: Set[str]) -> Tuple[str, ...]:
  aux_symbols = list(symbols)
  fused_symbols = []
  while len(aux_symbols) != 0:
    next_fused_symbols, processed_index = get_next_fused_symbols_and_index(
      aux_symbols, fusion_symbols, ignore)
    fused_symbols.append(next_fused_symbols)
    del aux_symbols[:processed_index + 1]
  return tuple(fused_symbols)


def get_next_fused_symbols_and_index(symbols: Tuple[str, ...], fusion_symbols: Set[str], ignore: Set[str]) -> Tuple[str, int]:
  first_symbol_without_ignore_symbols = strip_off_ignore(symbols[0], ignore)
  if first_symbol_without_ignore_symbols not in fusion_symbols:
    return symbols[0], 0
  fused_fusion_symbols, processed_index = get_next_consecutive_fusion_symbols_and_index(
    symbols, fusion_symbols, ignore)
  return fused_fusion_symbols, processed_index


def get_next_consecutive_fusion_symbols_and_index(symbols: Tuple[str, ...], fusion_symbols: Set[str], ignore: Set[str]) -> Tuple[str, int]:
  assert strip_off_ignore(symbols[0], ignore) in fusion_symbols
  consecutive_fusion_symbols = symbols[0]
  processed_index = 0
  for symbol in symbols[1:]:
    symbol_without_ignore = strip_off_ignore(symbol, ignore)
    if symbol_without_ignore in fusion_symbols:
      consecutive_fusion_symbols += symbol
      processed_index += 1
    else:
      break
  return consecutive_fusion_symbols, processed_index


def strip_off_ignore(symbol: str, ignore: Set[str]) -> str:
  for ignore_symbol in ignore:
    symbol = symbol.replace(ignore_symbol, "")
  return symbol


def parse_ipa_to_symbols(sentence: str) -> Tuple[str, ...]:
  all_symbols = tuple(sentence)
  return parse_ipa_symbols_to_symbols(all_symbols)


def parse_ipa_symbols_to_symbols(all_symbols: Tuple[str, ...]) -> Tuple[str, ...]:
  all_symbols = merge_together(
    symbols=all_symbols,
    merge_symbols=TIES,
    ignore_merge_symbols=PUNCTUATION_AND_WHITESPACE,
  )

  all_symbols = merge_right(
    symbols=all_symbols,
    merge_symbols=APPENDIX,
    ignore_merge_symbols=PUNCTUATION_AND_WHITESPACE,
    insert_symbol=None,
  )

  all_symbols = merge_left(
    symbols=all_symbols,
    merge_symbols=STRESSES,
    ignore_merge_symbols=PUNCTUATION_AND_WHITESPACE,
    insert_symbol=None,
  )

  return all_symbols


def merge_together(symbols: Tuple[str, ...], merge_symbols: Set[str], ignore_merge_symbols: Set[str]) -> Tuple[str, ...]:
  merge_or_ignore_merge_symbols = merge_symbols.union(ignore_merge_symbols)
  j = 0
  merged_symbols = []
  while j < len(symbols):
    new_symbol, j = get_next_merged_together_symbol_and_index(
      symbols, j, merge_symbols, merge_or_ignore_merge_symbols)
    merged_symbols.append(new_symbol)
  return tuple(merged_symbols)


def get_next_merged_together_symbol_and_index(symbols: Tuple[str, ...], j, merge_symbols: Set[str], merge_or_ignore_merge_symbols: Set[str]):
  assert merge_symbols.issubset(merge_or_ignore_merge_symbols)
  assert j < len(symbols)
  new_symbol = symbols[j]
  j += 1
  while symbols[j - 1] not in merge_or_ignore_merge_symbols and j < len(symbols):
    merge_symbol_concat, index = get_all_next_consecutive_merge_symbols(symbols[j:], merge_symbols)
    if len(merge_symbol_concat) > 0 and symbols[j + index] not in merge_or_ignore_merge_symbols:
      new_symbol += merge_symbol_concat + symbols[j + index]
      j += index + 1
    else:
      break
  return new_symbol, j


def get_all_next_consecutive_merge_symbols(symbols: Tuple[str, ...], merge_symbols: Set[str]) -> Tuple[str, int]:
  assert len(symbols) > 0
  merge_symbol_concat = ""
  index = None
  for index, symbol in enumerate(symbols):
    if symbol in merge_symbols:
      merge_symbol_concat += symbol
    else:
      return merge_symbol_concat, index
  assert index is not None
  return merge_symbol_concat, index


def merge_left(symbols: Tuple[str, ...], merge_symbols: Set[str], ignore_merge_symbols: Set[str], insert_symbol: Optional[str]) -> Tuple[str, ...]:
  if insert_symbol is None:
    insert_symbol = ""
  merged_symbols = merge_left_core(symbols, merge_symbols, ignore_merge_symbols)
  merged_symbols_with_insert_symbols = (
    insert_symbol.join(single_merged_symbols) for single_merged_symbols in merged_symbols)
  return tuple(merged_symbols_with_insert_symbols)


def merge_left_core(symbols: Tuple[str, ...], merge_symbols: Set[str], ignore_merge_symbols: Set[str]) -> Tuple[Tuple[str, ...]]:
  j = 0
  reversed_symbols = symbols[::-1]
  reversed_merged_symbols = []
  while j < len(reversed_symbols):
    new_symbol, j = get_next_merged_left_symbol_and_index(
      reversed_symbols, j, merge_symbols, ignore_merge_symbols)
    reversed_merged_symbols.append(new_symbol)
  merged_symbols = reversed_merged_symbols[::-1]
  return tuple(merged_symbols)


def get_next_merged_left_symbol_and_index(symbols: Tuple[str, ...], j: int, merge_symbols: Set[str], ignore_merge_symbols: Set[str]) -> Tuple[str, int]:
  new_symbol = [symbols[j]]
  j += 1
  if new_symbol[0] not in ignore_merge_symbols and new_symbol[0] not in merge_symbols:
    while j < len(symbols) and symbols[j] in merge_symbols:
      new_symbol.insert(0, symbols[j])
      j += 1
  return tuple(new_symbol), j


def merge_right(symbols: Tuple[str, ...], merge_symbols: Set[str], ignore_merge_symbols: Set[str], insert_symbol: Optional[str]) -> Tuple[str, ...]:
  if insert_symbol is None:
    insert_symbol = ""
  merged_symbols = merge_right_core(symbols, merge_symbols, ignore_merge_symbols)
  merged_symbols_with_insert_symbols = (
    insert_symbol.join(single_merged_symbols) for single_merged_symbols in merged_symbols)
  return tuple(merged_symbols_with_insert_symbols)


def merge_right_core(symbols: Tuple[str, ...], merge_symbols: Set[str], ignore_merge_symbols: Set[str]) -> Tuple[Tuple[str, ...]]:
  j = 0
  merged_symbols = []
  while j < len(symbols):
    new_symbol, j = get_next_merged_right_symbol_and_index(
      symbols, j, merge_symbols, ignore_merge_symbols)
    merged_symbols.append(new_symbol)
  return tuple(merged_symbols)


def get_next_merged_right_symbol_and_index(symbols: Tuple[str, ...], j: int, merge_symbols: Set[str], ignore_merge_symbols: Set[str]) -> Tuple[str, int]:
  new_symbol = [symbols[j]]
  j += 1
  if new_symbol[0] not in ignore_merge_symbols and new_symbol[0] not in merge_symbols:
    while j < len(symbols) and symbols[j] in merge_symbols:
      new_symbol.append(symbols[j])
      j += 1
  return tuple(new_symbol), j
