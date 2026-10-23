"""Move JPG images from a folder into a separate subfolder."""

from pathlib import Path
import shutil


def organize_jpg_files(folder: Path) -> int:
    """Move .jpg and .jpeg files in folder into its JPG Files subfolder."""
    destination = folder / "JPG Files"
    destination.mkdir(exist_ok=True)

    moved_count = 0

    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in {".jpg", ".jpeg"}:
            continue

        new_path = destination / file_path.name

        # Avoid overwriting a file with the same name.
        if new_path.exists():
            print(f"Skipped (already exists): {file_path.name}")
            continue

        shutil.move(str(file_path), str(new_path))
        print(f"Moved: {file_path.name}")
        moved_count += 1

    return moved_count


def main() -> None:
    folder_text = input("Enter the folder path to organize: ").strip().strip('"')
    folder = Path(folder_text).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("That folder does not exist. Check the path and try again.")
        return

    count = organize_jpg_files(folder)
    print(f"\nFinished. Moved {count} JPG/JPEG file(s).")


if __name__ == "__main__":
    main()
