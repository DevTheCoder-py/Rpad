import json
import os
import curses
import time
import sys
from utils import *
RED = "\033[31m"
RESET = "\033[0m"

def RW(mode, notes, FP):
    from utils import clear_screen
    if mode.upper() == "R":
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
                    clear_screen()
                    print(f"\nTitle: {note.get('title', 'Untitled')}\n")

                    for line_num, text in lines.items():
                        print(f"{RED}{line_num}{RESET}: {text}")

                    input("press enter to return")

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
    elif mode.upper() == "W":
        Write(notes, FP)
    elif "ls" == mode.lower() or "list" == mode.lower():
        clear_screen()
        print("i")
        for i in range(len(notes)):
            print(f"{i+1}: {notes[i]["title"]}")
            input(f"{RED}press enter to continue{RESET}")

    else:
        print("mode error")




def Write(notes, FP):
    from utils import uploadNote
    try:
        nn = input("Enter note number to write to (or Q to quit): ")
        if nn.upper() == "Q":
            return
        nn = int(nn)
        if nn <= len(notes):
            note = notes[nn - 1]
        else:
            note = {"title": f"Note{nn}", "lines":{}}

    except (ValueError, IndexError) as e:
        print(f"Invalid input: {e}")
        return

    def sub(stdscr):
        curses.curs_set(1)
        stdscr.keypad(True)
        
        lines = note.get("lines", {})
        # Convert lines to a list of strings for editing
        edit_lines = [lines.get(str(i), "") for i in range(1, len(lines) + 2)]

        y = 0
        x = 0
        
        while True:
            HEADER_LINES = 3
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            h, w = h-1, w-1
            curses.start_color()       # Enable color functionality
            curses.use_default_colors()
            curses.init_pair(1, curses.COLOR_RED, -1)  # Red text, default background
            curses.init_pair(2, curses.COLOR_GREEN, -1)
            stdscr.addstr(0, 0, "RPAD - Press Ctrl+D to save and exit", curses.color_pair(1))
            stdscr.addstr(1, 0, "Use arrow keys to navigate", curses.color_pair(2))  # second line of info
            stdscr.addstr(2,0, f"Title: {note['title']}")
            available_width = w - 4 - 1
            # Display lines
            # Display lines
            for i, line in enumerate(edit_lines):
                if i + HEADER_LINES < h:
                    line_num_str = f"{i+1}".rjust(4) + " "
                    stdscr.addstr(i + HEADER_LINES, 0, line_num_str, curses.color_pair(1))
                    stdscr.addstr(i + HEADER_LINES, len(line_num_str), line[:available_width])

            stdscr.move(y + HEADER_LINES, x+5) # for x maybe add 4 later for line num width
            stdscr.refresh()

            key = stdscr.getch()

            if key == (curses.KEY_UP):
                y = max(0, y - 1)
            elif key == (curses.KEY_DOWN):
                y = min(len(edit_lines) - 1, y + 1)
            elif key == (curses.KEY_LEFT):
                x = max(0, x - 1)
            elif key == (curses.KEY_RIGHT):
                x = min(len(edit_lines[y]), x + 1)
            elif key == curses.KEY_BACKSPACE or key == 127:
                if x > 0:
                    edit_lines[y] = edit_lines[y][:x - 1] + edit_lines[y][x:]
                    x -= 1
                elif y > 0:
                    x = len(edit_lines[y-1])
                    edit_lines[y-1] += edit_lines[y]
                    edit_lines.pop(y)
                    y -= 1
            elif key == curses.KEY_ENTER or key == 10:
                edit_lines.insert(y + 1, edit_lines[y][x:])
                edit_lines[y] = edit_lines[y][:x]
                y += 1
                x = 0
            elif 32 <= key <= 126:
                if x < available_width:
                    edit_lines[y] = edit_lines[y][:x] + chr(key) + edit_lines[y][x:] # text before curses + key + text after cursor
                    x += 1
            elif key == 4:
                # Save changes back to note
                new_lines = {}
                for i, line in enumerate(edit_lines):
                    if line: # Only save non-empty lines
                        new_lines[str(i + 1)] = line
                note["lines"] = new_lines
                break
    
    curses.wrapper(sub)
    uploadNote(FP, notes)
    
    
