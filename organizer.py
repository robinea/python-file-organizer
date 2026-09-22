# Python File Organizer
# Organizes files into folders based on their extensions.

from pathlib import Path
import shutil

folder = Path(input("Enter the folder path: "))
moved_count = 0
if not folder.exists():
    print("Folder does not exist.")
    exit()
for file in folder.iterdir():
    if file.is_file():
        extension = file.suffix.lower()
        folder_name = extension[1:] if extension else "unknown"
        destination = folder / folder_name
        destination.mkdir(exist_ok=True)
        target = destination / file.name
        if target.exists():
            print(f"Skipped: {file.name} already exists.")
        else:
            shutil.move(str(file), str(target))
            moved_count += 1
            print(f"Moved: {file.name} -> {folder_name}/")


print(f"\nFinished! {moved_count} file{'s' if moved_count != 1 else ''} moved.")