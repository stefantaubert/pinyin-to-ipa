# Contributing

If you notice an error, please don't hesitate to open an issue.

## Development setup

```sh
# update
sudo apt update
# install Python for ensuring that tests can be run
sudo apt install python3-pip \
  python3.8 python3.8-dev python3.8-distutils python3.8-venv \
  python3.9 python3.9-dev python3.9-distutils python3.9-venv \
  python3.10 python3.10-dev python3.10-distutils python3.10-venv \
  python3.11 python3.11-dev python3.11-distutils python3.11-venv \
  python3.12 python3.12-dev python3.12-distutils python3.12-venv \
  python3.13 python3.13-dev python3.13-venv

# check out repo
git clone https://github.com/stefantaubert/pinyin-to-ipa.git
cd pinyin-to-ipa
# create virtual environment
python3.13 -m venv .venv-py13
source .venv-py13/bin/activate
pip install -e .[dev,app]
```

## Running the tests

```sh
mkdir coverage
coverage erase
tox
coverage combine
coverage html -d coverage
coverage report -m
```
