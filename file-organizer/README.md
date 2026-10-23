# JPG File Organizer

A simple Python automation script that moves `.jpg` and `.jpeg` images from a selected folder into a `JPG Files` subfolder.

# Features

- Organizes JPG and JPEG files.
- Keeps other file types in place.
- Skips files if a same-named file already exists in the destination.

# Requirements

- Python 3
- No additional packages required

# How to run

1. Run `file_organizer.py`.
2. Enter the path of the folder containing the files.
3. The script creates a `JPG Files` folder and moves matching images into it.

# Example

```text
Before:
tempfolder/
├── praj.jpg
└── note.txt

After:
tempfolder/
├── JPG Files/
│   └── praj.jpg
└── note.txt