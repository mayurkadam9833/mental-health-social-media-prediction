from src.mental_health_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.mental_health_prediction.pipeline.data_validation_pipeline import DataValidationPipeline
from src.mental_health_prediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.mental_health_prediction.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.mental_health_prediction.logging import logger

# data ingestion pipeline execution
stage_one="Data Ingestion"
if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_one} completed >>>>\n")
    except Exception as e: 
        logger.info(e)
        raise e 
    

# data validation pipeline execution
stage_two="Data Validation"
if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_two} started >>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_two} completed >>>>\n")
    except Exception as e: 
        logger.info(e)
        raise e 

# data transformation pipeline execution
stage_three="Data Transformation"
if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_three} started >>>>")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_three} completed >>>>\n")
    except Exception as e: 
        logger.info(e)
        raise e 

# Model Training pipeline execution
stage_four="Model Trainer"
if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage:{stage_four} started >>>>")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_four} completed >>>>\n")
    except Exception as e: 
        logger.info(e)
        raise e 