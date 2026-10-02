#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if ! python3 scripts/refresh_github_stars.py; then
  echo "Building with the last saved GitHub star counts." >&2
fi
bundle exec jekyll build "$@"
