#!/usr/bin/env bash

if [[ ! -f venv ]]; then
  python -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt

echo
python test.py Dockerfile
echo
python test.py Dockerfile.ok
