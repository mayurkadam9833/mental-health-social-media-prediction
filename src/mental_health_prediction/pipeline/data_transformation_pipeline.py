from src.mental_health_prediction.components.Data_Transformation import DataTransformation 
from src.mental_health_prediction.config.configuration import ConfigManager 

"""
DataTransformationPipeline class is pipeline to read extract data,drop columns not required,encode categorical data, 
split data into test and train apply oversampling and scaling
"""
class DataTransformationPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()                                                     # create object of configmanager
        data_transformation_config=config.get_data_transformation_config()         # get data transformation config
        data_transformation=DataTransformation(config=data_transformation_config)  # create object of DataTransformation
        data_transformation.drop_col()                                             # drop columns not required 
        data_transformation.encode_data()                                          # encode categorical data into numeric
        data_transformation.train_test_split()                                     # split data into train and test [train_test_split,oversampling,scaling]
