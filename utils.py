import os
import shutil
from datetime import datetime


def organize_by_type(folder: str, dry_run: bool = False, summary: bool = False) -> int:
    count = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        ext = filename.split('.')[-1].lower()
        target_folder = os.path.join(folder, ext)

        if not summary:
            print(f"{'Would move' if dry_run else 'Moved'} {filename} -> {ext}/")

        if not dry_run:
            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
            except (PermissionError, shutil.Error) as e:
                print(f"⚠️ Skipped '{filename}': {e}")
                continue

        count += 1
    return count


def organize_by_date(folder: str, dry_run: bool = False, summary: bool = False) -> int:
    count = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if not os.path.isfile(file_path):
            continue

        mod_time = os.path.getmtime(file_path)
        date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
        target_folder = os.path.join(folder, date_folder)

        if not summary:
            print(f"{'Would move' if dry_run else 'Moved'} {filename} -> {date_folder}/")

        if not dry_run:
            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
            except (PermissionError, shutil.Error) as e:
                print(f"⚠️ Skipped '{filename}': {e}")
                continue

        count += 1
    return count
