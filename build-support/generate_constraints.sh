#!/usr/bin/env bash
# Copyright 2020 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# See https://www.pantsbuild.org/v2.0/docs/python-third-party-dependencies.

set -euo pipefail

python -m pip install pip==21.2.2 pip-tools==6.5.0

REQIN_FILES="common-requirements.txt $(find 3rdparty -name '*requirements.txt' | tr '\n' ' ')"
echo "using requirements from... ${REQIN_FILES}"

echo "compiling constraints file"
python -m piptools compile -o constraints.txt --no-header --no-annotate --strip-extras ${REQIN_FILES}