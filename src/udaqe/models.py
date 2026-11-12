from dataclasses import dataclass

@dataclass
class DatasetMetadata:
    name: str
    file_path: str
    file_format: str
    row_count: int | None = None
    column_count: int