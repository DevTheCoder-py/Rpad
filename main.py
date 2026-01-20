import json
import os

file_path = "data.json"

with open(file_path, "r") as f:
    notes = json.load(f)
new_note = [
        {
            "title": "sample",
            "lines": {
                1: "yo",
                2: "yor"
                }
            }
        ]
print(notes)
notes.append(new_note)
with open(file_path, "w") as f:
    json.dump(notes, f, indent=4)
