# Command Line Utility 🛠️

## Overview

Fancy seeing you here! 👋

I thought it would be cool to challenge myself by creating some handy command-line utilities for renaming files and searching for text patterns within files in a specified directory. This project is all about having fun while coding and improving my Python skills!

## What Can These Scripts Be Used For? 🤔

These scripts are super versatile and can be used for a variety of tasks in different projects:

- **Organizing Files:** Use the renaming script to keep your files neat and orderly. Great for photo collections, document archives, or any project with lots of files!
- **Text Analysis:** The search script can help you find specific text patterns across many files. Perfect for analyzing logs, codebases, or any text-heavy data.
- **Pre-processing Data:** Preparing data for other projects? Filter and rename files quickly to fit your needs.
- **Automation:** Integrate these scripts into larger automation workflows for repetitive file management tasks.

## Installation

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/MuxN4/command_line_utils.git
    ```
2. Navigate to the project directory:
    ```bash
    cd handy_helper_scripts
    ```
3. (Optional) Create a virtual environment:
    You don't have to, heck, you don't even need to – it's just good practice!
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

## Usage

### Rename Files 📁

This script allows you to rename files in a specified directory based on given patterns and optional filters (like extensions, sizes, and modification dates).

```bash
python rename_files/rename.py ~/New\ folder --pattern 'new_hello.py'

2024-07-03 21:35:19,491 - INFO - Renamed /home/steve/New folder/hello.py to /home/steve/New folder/new_hello.py
```

### Conclusion

I hope you find these scripts as fun and useful as I do!Feel free to further customize it to fit your preferences or project specifics!
