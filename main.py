import json
import os
import time
import curses
from utils import *
from RW import *
FP = "data.json"
#Colors
RED = "\033[31m"
RESET = "\033[0m"
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
