from pathlib import Path

def get_file_format(file_path: str) -> str:
    file_format = Path(file_path).suffix.lstrip(".").lower()

    if not file_format:
        raise ValueError("File path must have a valid file extension")

    return file_format