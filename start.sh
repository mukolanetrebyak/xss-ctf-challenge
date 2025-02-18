#!/bin/bash

source /home/mykola-cs/Документи/scripts/xss-ctf-challenge/env/bin/activate
nohup python3 /home/mykola-cs/Документи/scripts/xss-ctf-challenge/wsgi.py >/dev/null 2>&1 &
