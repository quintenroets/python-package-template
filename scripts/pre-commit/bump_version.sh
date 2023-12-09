#!/usr/bin/env bash

if ! git diff --staged pyproject.toml | grep -q version; then
    bump2version --config-file .bumpversion.cfg patch
fi
