#!/usr/bin/env bash

echo "Deleting .venv folder"
rm -rf .venv/

echo "Creating new virtual enviroment at .venv/"
python3 -m venv .venv/

echo "Activating .venv"
source .venv/bin/activate

if [[ "$OSTYPE" == "darwin"* ]]; then
  CFLAGS="-I$(brew --prefix)/include" LDFLAGS="-L$(brew --prefix)/lib" pip install mysqlclient
fi

echo "Installing all required dependencies..."
pip install -r requirements.txt

echo "Upgrading pip..."
pip install --upgrade pip




