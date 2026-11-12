from dataclasses import dataclass

@dataclass
class DatasetMetadata:
    name: str
    file_path: str
    file_format: str
    row_count: int | 
    column_count: int