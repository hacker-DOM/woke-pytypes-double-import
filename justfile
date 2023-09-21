#!/usr/bin/env just --justfile
# https://github.com/casey/just
# Also `brew install just`

# It seems that on MacOS, just will use `zsh` to run commands (recipes).
# I think it uses the system's default shell. To make sure it's consistent,
# let's set it explicitly.
set shell := ["zsh", "-c"]

setup:
    set -e;
    python3 -m venv .venv;
    source .venv/bin/activate;
    pip install -r requirements.txt;

run:
    set -e;
    woke init pytypes;
    rg 'from __future' pytypes;

