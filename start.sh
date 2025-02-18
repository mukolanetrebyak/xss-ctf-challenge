#!/bin/bash

source env/bin/activate
nohup python3 wsgi.py >/dev/null 2>&1 &
