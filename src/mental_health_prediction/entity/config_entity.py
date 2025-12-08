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


"""
Entity: DataValidationConfig
Description:
Represents the configuration parameters required for the Data Validation stage. 
This entity holds paths of extracted dataset files, defined schema, validation status text file
"""
@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir:Path 
    unzip_data: Path
    status:str
    all_schema: dict


"""
Entity: DataTransformationConfig
Description:
Represents the configuration parameters required for the Data Transformation stage. 
This entity holds paths of extracted dataset file, target column
"""
@dataclass(frozen=True)
class DataTransformationConfig: 
    root_dir:Path
    data_path:Path
    target_col: str   

"""
Entity: ModelTrainerConfig
Description:
Represents the configuration parameters required for the Model training stage. 
This entity holds paths of train dataset, target column, parameters of model
"""
@dataclass(frozen=True) 
class ModelTrainerConfig: 
    root_dir: Path 
    train_data: Path 
    target_col: str 
    algorithm: str 
    n_neighbors: int
    weights: str 