#!/usr/bin/env bash

mkdir -p interim

CSVPATH='https://docs.google.com/spreadsheets/d/1CwFdeJlGGZU3w8pUTMV43EdyKcTPFoz3c1Jns0_xd8A/export?format=csv'

wget --no-check-certificate -O interim/lm_stats.csv $CSVPATH
python format_md.py

csv2md interim/lm_stats.csv > interim/table.md

cat interim/header.md interim/table.md interim/mid.md interim/legend.md > index.md
