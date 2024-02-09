# pinyin-to-ipa

[![PyPI](https://img.shields.io/pypi/v/pinyin-to-ipa.svg)](https://pypi.python.org/pypi/pinyin-to-ipa)
[![PyPI](https://img.shields.io/pypi/pyversions/pinyin-to-ipa.svg)](https://pypi.python.org/pypi/pinyin-to-ipa)
[![MIT](https://img.shields.io/github/license/stefantaubert/pinyin-to-ipa.svg)](https://github.com/stefantaubert/pinyin-to-ipa/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/wheel/pinyin-to-ipa.svg)](https://pypi.python.org/pypi/pinyin-to-ipa)
[![PyPI](https://img.shields.io/pypi/implementation/pinyin-to-ipa.svg)](https://pypi.python.org/pypi/pinyin-to-ipa)
[![PyPI](https://img.shields.io/github/commits-since/stefantaubert/pinyin-to-ipa/latest/master.svg)](https://github.com/stefantaubert/pinyin-to-ipa/compare/v0.0.2...master)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10639971.svg)](https://doi.org/10.5281/zenodo.10639971)

Command-line interface (CLI) and Python library to transcribe pinyin to IPA.
The tones are attached to the vowel of the syllable.

## Installation

```sh
pip install pinyin-to-ipa --user
```

## Usage

```txt
usage: pinyin-to-ipa-cli [-h] [-v] [--sep SEP] [--first] PINYIN

Command-line interface (CLI) to transcribe pinyin to IPA.

positional arguments:
  PINYIN         pinyin

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  --sep SEP      separator between phonemes (default: )
  --first        return only first result (default: False)
```

### Example

```sh
$ pinyin-to-ipa-cli "pang1" 
pʰa˥ŋ
$ pinyin-to-ipa-cli "pang2" 
pʰa˧˥ŋ
$ pinyin-to-ipa-cli "pang3" 
pʰa˧˩˧ŋ
$ pinyin-to-ipa-cli "pang4" 
pʰa˥˩ŋ
$ pinyin-to-ipa-cli "pang5" 
pʰaŋ
$ pinyin-to-ipa-cli "pang" 
pʰaŋ
$ pinyin-to-ipa-cli "hàng" 
xa˥˩ŋ
ha˥˩ŋ
$ pinyin-to-ipa-cli "hàng" --first
xa˥˩ŋ
$ pinyin-to-ipa-cli "hng" 
hŋ
$ pinyin-to-ipa-cli "test" 
No IPA transcription available!
```

Usage as library:

```py
from pinyin_to_ipa import pinyin_to_ipa

print(pinyin_to_ipa("hang4"))
# OrderedSet([('x', 'a˥˩', 'ŋ'), ('h', 'a˥˩', 'ŋ')])

print(pinyin_to_ipa("ng"))
# OrderedSet([('ŋ',)])
```

## Phoneme Set

Vowels:

```txt
a
ɛ
e
ə
ɚ
ɤ
i
o
u
ʊ
y
```

Diphthongs:

```txt
ai̯
au̯
aɚ̯¹
ei̯
ou̯
```

Consonants:

```txt
f
h¹
j
k
kʰ
l
m
n
p
pʰ
ɹ̩²
ɻ²
ɻ̩²
s
t
ts
tsʰ
tɕ
tɕʰ
tʰ
w
x
ŋ
ɕ
ɥ
ʂ
ʈʂ
ʈʂʰ
z̩¹²
ʐ¹²
ʐ̩¹²
```

Vowels and diphthongs contain one of these tones:

```txt
˥ (first tone)
˧˥ (second tone)
˧˩˧ (third tone)
˥˩ (fourth tone)
(none)
```

¹ These phonemes are not included if only the first transcription is used. \
² These consonants contain also tones.

## References

- [https://en.wikipedia.org/wiki/Help:IPA/Mandarin](https://en.wikipedia.org/wiki/Help:IPA/Mandarin)
- [https://en.wikipedia.org/wiki/Standard_Chinese_phonology](https://en.wikipedia.org/wiki/Standard_Chinese_phonology)
- [https://en.wikipedia.org/wiki/Pinyin](https://en.wikipedia.org/wiki/Pinyin)
- [https://de.wikipedia.org/wiki/Pinyin](https://de.wikipedia.org/wiki/Pinyin)
- Duanmu, San. 2007. The Phonology of Standard Chinese. 2nd ed. Oxford ; New York: Oxford University Press.
- Lin, Yen-Hwei. 2007. The Sounds of Chinese. Cambridge, UK ; New York: Cambridge University Press.

## Acknowledgments

[pypinyin](https://github.com/mozillazg/python-pinyin) \
Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project-ID 416228727 – CRC 1410

## Citation

If you want to cite this repo, you can use this BibTeX-entry generated by GitHub (see *About => Cite this repository*).

```txt
Taubert, S. (2024). pinyin-to-ipa (Version 0.0.2) [Computer software]. https://doi.org/10.5281/zenodo.10639971
```
