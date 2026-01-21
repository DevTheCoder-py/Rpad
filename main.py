import json
import os
import time
import curser
from utils import *
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


def AskUser():
    mode = input("Notepad Mode?\n R or W;\n")
    if mode == "R" or mode == "W":
        return mode
    else:
        print("Please input valid mode")
        clear_screen()
        time.sleep(1)
        AskUser()
clear_screen()
mode = AskUser()
notes = loadNote(FP)
RW(mode, notes)
#todo planning to use stdscr to make nano like text editor
