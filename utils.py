
import json
import os
import time
RED = "\033[31m"
RESET = "\033[0m"

def AskUser():
    try:
        clear_screen()
        mode = input("Notepad Mode?\n R or W;\n")
        if mode == "R" or mode == "W":
            return mode
        else:
            print("Please input valid mode")
            clear_screen()
            time.sleep(1)
            AskUser()
    except KeyboardInterrupt:
        print("Closing!")

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

