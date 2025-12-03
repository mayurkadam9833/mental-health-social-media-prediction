from src.mental_health_prediction.config.configuration import ConfigManager
from src.mental_health_prediction.components.Data_Ingestion import DataIngestion

"""
DataIngestionPipeline class is pipeline to download file and extract file in define folder
"""
class DataIngestionPipeline: 
    def __init__(self):
        pass

    def main(self):  
        config=ConfigManager()                                         # create object of configmanager
        data_ingestion_config=config.get_data_ingestion_config()       # get data ingsetion config
        data_ingestion=DataIngestion(config=data_ingestion_config)     # create object of DataIngestion
        data_ingestion.download_file()                                 # download data file 
        data_ingestion.extract_file()                                  # extract zip file