import json
import os
import time
RED = "\033[31m"
RESET = "\033[0m"

def RW(mode, notes):
    if mode == "R":
        if not notes:
            print("No notes available.")
        else:
            while True:
                try:
                    nn = input("Enter note number (or Q to quit): ")

                    if nn.upper() == "Q":
                        break

                    nn = int(nn)

                    note = notes[nn - 1]
                    lines = note["lines"]

                    print(f"\nTitle: {note.get('title', 'Untitled')}\n")

                    for line_num, text in lines.items():
                        print(f"{RED}{line_num}{RESET}: {text}")

                    break  # exit after successful read

                except ValueError:
                    print("Please enter a valid number.")

                except IndexError:
                    print("Note number out of range.")

                except KeyError:
                    print("Corrupted note format (missing 'lines').")

                except TypeError:
                    print("Invalid note data.")

                except Exception as e:
                    print(f"Unexpected error: {e}")
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

