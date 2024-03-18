#!/bin/sh
# Compile AutoSINTA into a Linux executable
pyinstaller main.py --clean --log-level INFO --onefile --windowed --name autosinta-v1.0.0-pyinstaller-linux
