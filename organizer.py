#!/usr/bin/env python3
"""
File Organizer CLI Tool
-----------------------
Organizes files in a folder by type (extension) or by modified date.

Usage:
    python organizer.py --path test_files --mode type
    python organizer.py --path test_files --mode date
"""

import os
import argparse
from utils import organize_by_type, organize_by_date


def main():
    parser = argparse.ArgumentParser(
        description="Organize files by type (extension) or date."
    )
    parser.add_argument(
        "--path", "-p", required=True,
        help="Path to the folder containing files."
    )
    parser.add_argument(
        "--mode", "-m", choices=["type", "date"], required=True,
        help="Organize by 'type' or 'date'."
    )

    args = parser.parse_args()
    folder = args.path
    mode = args.mode

    if not os.path.exists(folder):
        print(f"Error: The folder '{folder}' does not exist.")
        return

    if mode == "type":
        moved = organize_by_type(folder)
    else:
        moved = organize_by_date(folder)

    print(f"\nDone! Organized {moved} files in '{folder}' by {mode}.")


if __name__ == "__main__":
    main()
