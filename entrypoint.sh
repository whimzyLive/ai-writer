#!/usr/bin/env bash
set -e
set -o pipefail

echo ">>> Preparing blog writer..."

./src/main.py

# bash -c "set -e;  set -o pipefail; $1"
