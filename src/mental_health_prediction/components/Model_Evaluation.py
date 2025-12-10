import os
import joblib 
import pandas as pd 
from pathlib import Path
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score
from src.mental_health_prediction.utils.common import save_json
from src.mental_health_prediction.entity.config_entity import ModelEvaluationConfig
from src.mental_health_prediction.logging import logger 


"""
ModelEvaluation class contain method for 
evaluation on test data it will return json file which contain all classification metrics scores
"""
class ModelEvaluation: 
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config 
        self.model=joblib.load(self.config.model_path)
    
    # method for return all metrics for classification
    def get_metrics(self,actual,predicted): 
        acc=accuracy_score(actual,predicted)
        cf=confusion_matrix(actual,predicted)
        pr=precision_score(actual,predicted,average="weighted")
        rc=recall_score(actual,predicted,average="weighted")
        f1=f1_score(actual,predicted,average="weighted")
        return acc,cf,pr,rc,f1
    
    # model evaluation method
    def evaluation(self): 
        try: 
            # read data from test data
            data=pd.read_csv(self.config.test_data)

            # split data into target and input features
            test_x=data.drop([self.config.target_col],axis=1)
            test_y=data[self.config.target_col]

            # make prediction
            test_pred=self.model.predict(test_x)
            
            # all metrics
            acc,cf,pr,rc,f1=self.get_metrics(test_y,test_pred)

            # metrics in dict format
            scores={"accuracy":acc,"confusion matrix":cf.tolist(),"precision score":pr,"recall":rc,"f1-score":f1}

            # saved metrics json file 
            save_json(scores,Path(self.config.evaluation))
        
        except Exception as e: 
            raise e