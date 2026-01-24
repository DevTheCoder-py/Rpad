#!/usr/bin/env python3
import json
import os
import time
import curses
import signal
import sys
import subprocess
from utils import *
from RW import *
global FP
FP = "./data.json"
RED = "\033[31m"
RESET = "\033[0m"

#Colors
def handle_sigint(sig, frame):
    print(f"\n{RED}Exiting…")  # clean message
    if not os.name == "nt":
        user_shell = os.environ.get("SHELL")
        if user_shell:    
            subprocess.run([user_shell])

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
if not os.path.exists(FP):
    with open(FP, "w") as f:
        json.dump([], f)
    notes = []
else:
    with open(FP, "r") as f:
        notes = json.load(f)

mainScr(FP)
#todo planning to use stdscr to make nano like text editor
