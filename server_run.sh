#!/bin/bash

## Environment Setup
python3.8 -m venv ../env
source ../env/bin/activate
pip install -r requirements.txt

python manage.py runserver 8081