#!/bin/bash
# File: run.sh
# Created on: 7/4/2017
# Created by: Matt Gambill
# Synopsis: combines files and run jsonParse.py
cat ./books/*.csv > books.csv
python jsonParse.py
