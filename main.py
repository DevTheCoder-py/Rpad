#!/usr/bin/env python3
import json
import os
import time
import curses
import signal
import sys
from utils import *
from RW import *
FP = "./data.json"
RED = "\033[31m"
RESET = "\033[0m"

#Colors
def handle_sigint(sig, frame):
    print(f"\n{RED}Exiting…")  # clean message
    sys.exit(0)

# Catch Ctrl+C everywhere
signal.signal(signal.SIGINT, handle_sigint)
######
# Sample in case i forget
sample_note = {
    "title": "test",
    "lines": {
        "1": "yo",
        "2": "yor"
    }
}
if os.path.exists(FP):
    with open(FP, "r") as f:
        notes = json.load(f)
else:
    notes = []


clear_screen()
mode = AskUser()
notes = loadNote(FP)
RW(mode, notes)
#todo planning to use stdscr to make nano like text editor
