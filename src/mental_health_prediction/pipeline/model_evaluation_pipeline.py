from src.mental_health_prediction.components.Model_Evaluation import ModelEvaluation 
from src.mental_health_prediction.config.configuration import ConfigManager 

"""
ModelEvaluationPipeline class is pipeline to evaluate model on test data
"""
class ModelEvaluationPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()                                                     # create object of configmanager
        model_evalutaion_config=config.get_model_evaluation_config()               # get model evaluation config
        model_evalution=ModelEvaluation(config=model_evalutaion_config)            # create object of ModelEvaluation
        model_evalution.evaluation()                                               # model evaluation