import os 
import pandas as pd 
from src.mental_health_prediction.entity.config_entity import DataValidationConfig
from src.mental_health_prediction.logging import logger

"""
DataValidation class contain method for 
validation of dataset schema
"""
class DataValidation: 
    def __init__(self,config:DataValidationConfig):
        self.config=config 

    # method for validation schema of dataset with defined schema
    def schema_validation(self): 
        try: 
            # load extracted data
            data=pd.read_csv(self.config.unzip_data)
            # all columns in dataset
            all_col=list(data.columns) 
            #  defined schema
            schema=list(self.config.all_schema.keys())
            schema_validation=True 

            # create loop if column not in defined schema it will return False
            for col in all_col: 
                if col == "mental_state": 
                    continue

                if col not in schema: 
                    schema_validation=False 

            # write schema validation status in file 
            with open(self.config.status,"w")as file: 
                file.write(f"schema validation status:{schema_validation}")
            
            logger.info(f"schema validation completed")
        
        except Exception as e : 
            raise e 
        
