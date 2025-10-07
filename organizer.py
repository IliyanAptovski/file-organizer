#!/usr/bin/env python3
"""
File Organizer CLI Tool
-----------------------
Organizes files in a folder by type (extension) or by modified date.

Usage:
    python organizer.py --path test_files --mode type [--dry-run] [--summary]
    python organizer.py --path test_files --mode date [--dry-run] [--summary]
"""

import os
import argparse
from utils import organize_by_type, organize_by_date


def main():
    parser = argparse.ArgumentParser(
        description="Organize files by type (extension) or by modified date."
    )
    parser.add_argument("--path", "-p", required=True, help="Path to the folder containing files.")
    parser.add_argument("--mode", "-m", choices=["type", "date"], required=True, help="Organize by 'type' or 'date'.")
    parser.add_argument("--dry-run", action="store_true", help="Preview file moves without actually moving files.")
    parser.add_argument("--summary", action="store_true", help="Show only a summary of results (no detailed output).")

    args = parser.parse_args()
    folder, mode, dry_run, summary = args.path, args.mode, args.dry_run, args.summary

    # --- Error handling and validations ---
    if not os.path.exists(folder):
        print(f"❌ Error: The folder '{folder}' does not exist.")
        return

    if not os.path.isdir(folder):
        print(f"⚠️ Warning: '{folder}' is not a directory.")
        return

    if not os.listdir(folder):
        print(f"📁 The folder '{folder}' is empty. Nothing to organize.")
        return

    try:
        if mode == "type":
            moved = organize_by_type(folder, dry_run=dry_run, summary=summary)
        else:
            moved = organize_by_date(folder, dry_run=dry_run, summary=summary)

        action = "Would have organized" if dry_run else "Organized"
        print(f"\n✅ {action} {moved} files in '{folder}' by {mode}.")

    except PermissionError:
        print("🚫 Permission denied. Please check your folder permissions.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
