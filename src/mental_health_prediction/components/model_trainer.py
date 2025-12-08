import os 
import pandas as pd 
import joblib
from sklearn.neighbors import KNeighborsClassifier
from src.mental_health_prediction.entity.config_entity import ModelTrainerConfig
from src.mental_health_prediction.logging import logger

"""
ModelTrainer class contain method for 
train model on train dataset and saved trained model
"""
class ModelTrainer: 
    def __init__(self,config:ModelTrainerConfig):
        self.config=config 
        self.model=KNeighborsClassifier(algorithm=self.config.algorithm,n_neighbors=self.config.n_neighbors,weights=self.config.weights)
    
    #  method for train model on train dataset
    def train(self): 
        try: 
            # read train data
            data=pd.read_csv(self.config.train_data)

            # divide data into input and target
            train_x=data.drop([self.config.target_col],axis=1)
            train_y=data[self.config.target_col]

            # train model
            model=self.model.fit(train_x,train_y)

            # saved train model
            joblib.dump(model,os.path.join(self.config.root_dir,"model.joblib"))

            logger.info("model train and saved sucessfully")
        
        except Exception as e :
            raise e 
