#!/bin/bash

mkdir -p data

python -m scripts.migrate

exec "$@"