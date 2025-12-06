import os 
import joblib 
from pathlib import Path
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from src.mental_health_prediction.entity.config_entity import DataTransformationConfig
from src.mental_health_prediction.logging import logger

"""
DataTransformation class contain method for 
drop irrealvent features, encode categorical data to numeric,
train test split with oversampling and scaling
"""
class DataTransformation: 
    def __init__(self,config:DataTransformationConfig):
        self.config=config 
        self.gender_encode=OneHotEncoder(sparse_output=False)
        self.platform_encode=OneHotEncoder(sparse_output=False)
        self.scale=StandardScaler()
        self.sampling=SMOTE()

    # method for drop columns not required predictive analysis
    def drop_col(self):  
        # read csv file
        data=pd.read_csv(self.config.data_path)
        # dropping irrealvent columns
        data.drop(["person_name","date"],axis=1,inplace=True) 
        return data 
    
    # method for encode categorical data to numeric by using onehotencoder
    def encode_data(self): 
        data=self.drop_col()
        # encode actegorical data to numeric
        data=pd.concat([data.drop(["gender"],axis=1),pd.DataFrame(self.gender_encode.fit_transform(data[["gender"]]),columns=self.gender_encode.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["platform"],axis=1),pd.DataFrame(self.platform_encode.fit_transform(data[["platform"]]),columns=self.platform_encode.get_feature_names_out())],axis=1)
        return data 
    
    # method for split data into train and test, perform oversampling, scaling
    def train_test_split(self): 
        data=self.encode_data()

        # divide data into input features and target feature
        x=data.drop([self.config.target_col],axis=1)
        y=data[self.config.target_col]

        # split data into train and test
        train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=42)

        # apply oversampling on train data
        sample_train_x,sample_train_y=self.sampling.fit_resample(train_x,train_y)

        # apply StandardScaler on input features
        scale_train_x=self.scale.fit_transform(sample_train_x)
        scale_test_x=self.scale.transform(test_x)

        # concat input and target features
        train_data=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),pd.Series(sample_train_y).reset_index(drop=True)],axis=1)
        test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),pd.Series(test_y).reset_index(drop=True)],axis=1)

        # saved train and test data in csv format to data transformation folder
        train_data.to_csv(os.path.join(self.config.root_dir,"train_data.csv"),index=False)
        test_data.to_csv(os.path.join(self.config.root_dir,"test_data.csv"),index=False)

        logger.info("Data split sucessfully")
        logger.info(f"train data shape:{train_data.shape}")
        logger.info(f"test data shape:{test_data.shape}")