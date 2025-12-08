from src.mental_health_prediction.config.configuration import ConfigManager 
from src.mental_health_prediction.components.model_trainer import ModelTrainer 

"""
ModelTrainerPipeline class is pipeline to train model on training dataset
"""
class ModelTrainerPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()                                       # create object of configmanager
        model_trainer_config=config.get_model_trainer_config()       # get model trainer config
        model_trainer=ModelTrainer(config=model_trainer_config)      # create object of ModelTrainer
        model_trainer.train()                                        # model training