#!/bin/sh

pip3 virtualenv

python3 -m virtualenv virtualenv

source virtualenv/bin/activate

pip3 install -r requirements.txt

python app.py