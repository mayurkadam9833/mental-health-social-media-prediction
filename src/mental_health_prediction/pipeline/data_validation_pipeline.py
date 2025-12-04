from src.mental_health_prediction.config.configuration import ConfigManager
from src.mental_health_prediction.components.Data_Validation import DataValidation

"""
DataValidationPipeline class is pipeline to validate schema of downloaded dataset
"""
class DataValidationPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()                                              # create object of configmanager
        data_validation_config=config.get_data_validation_config()          # get data validation config
        data_validation=DataValidation(config=data_validation_config)       # create object of DataValidation 
        data_validation.schema_validation()                                 # schema validation