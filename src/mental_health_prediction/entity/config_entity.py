from pathlib import Path 
from dataclasses import dataclass 

"""
Entity: DataIngestionConfig
Description:
Represents the configuration parameters required for the Data Ingestion stage. 
This entity holds paths and URLs needed to download, store, and extract dataset files
"""
@dataclass(frozen=True) 
class DataIngestionConfig: 
    root_dir:Path 
    source_url:str
    local_data_path: Path
    unzip_dir:Path

