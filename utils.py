from RW import *
import json
import os
import time
RED = "\033[31m"
RESET = "\033[0m"
def AskUser():
    while True:
        try:
            clear_screen()
            mode = input("Notepad Mode?\n R, W or Q to quit;\n")
            if mode.upper() in ["R", "W", "LS", "LIST"]:
                return mode
            elif mode.upper() == "Q":
                print("Exiting...")
                exit(0)
            else:
                print("Please input a valid mode")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Closing!")
            exit(0)

def uploadNote(file_path, nt):
    with open(file_path, "w") as f:
        json.dump(nt, f, indent=4)
def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux, macOS, and other POSIX systems
        _ = os.system('clear')
def loadNote(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
def mainScr(FP):
    while True:
        clear_screen()
        mode = AskUser()
        notes = loadNote(FP)
        RW(mode, notes, FP)

