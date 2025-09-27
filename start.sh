#!/bin/bash
export $(grep -v '^#' .env | xargs)
python3 bot.py
