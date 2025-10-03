import os
import shutil
from datetime import datetime


def organize_by_type(folder: str, dry_run: bool = False) -> int:
    """Organize files in the folder into subfolders by file extension."""
    count = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            target_folder = os.path.join(folder, ext)
            if dry_run:
                print(f"Would move {filename} -> {ext}/")
            else:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} -> {ext}/")
            count += 1
    return count


def organize_by_date(folder: str, dry_run: bool = False) -> int:
    """Organize files in the folder into subfolders by modified date (YYYY-MM-DD)."""
    count = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
            target_folder = os.path.join(folder, date_folder)
            if dry_run:
                print(f"Would move {filename} -> {date_folder}/")
            else:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} -> {date_folder}/")
            count += 1
    return count
