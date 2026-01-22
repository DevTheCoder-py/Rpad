import json
import os
import curses
import time
from utils import *
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

                    input("press enter to return")
                    AskUser()# exit after successful read

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
    elif mode == "W":
        Write(notes)




def Write(notes):
    def sub(stdscr):
        row = 0
        for key, line in notes[0]["lines"].items():
            stdscr.addstr(row, 0, f"{key}: {line}")
            row += 1
        stdscr.refresh()
        stdscr.getch()
    
    curses.wrapper(sub)

    
