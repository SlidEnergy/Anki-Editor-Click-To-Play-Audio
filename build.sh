#!/usr/bin/env bash

cd "$(dirname "$0")"

./update-version-py.sh

rm -rf dist
mkdir dist

VERSION=$(git describe --tags --always --dirty)

cd src
zip -r9 "../dist/Editor-Click-To-Play-Audio_$VERSION.ankiaddon" . -x \*/__pycache__/\* \*/\*.pyc \*/\*.pyo \*/\*.pyd meta.json user_files/\*
cd ..
