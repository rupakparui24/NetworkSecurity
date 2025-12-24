from dataclasses import dataclass

@dataclass
class DataIngestionArctifact:
    training_file_path: str
    testing_file_path: str