from textSum.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSum.pipeline.stage_02_data_validation import DataValidationPipeline
from textSum.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSum.pipeline.stage_04_model_training import ModelTrainingPipeline
from textSum.logging import logger

STAGE_NAME = "DATA INGESTION"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>>>>")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} finished <<<<<<<<\n===============================")
except Exception as e: 
    logger.exception(e)
    raise e


STAGE_NAME = "DATA VALIDATION"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>>>>")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} finished <<<<<<<<\n===============================")
except Exception as e: 
    logger.exception(e)
    raise e



STAGE_NAME = "DATA TRANSFORMATION"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>>>>")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} finished <<<<<<<<\n===============================")
except Exception as e: 
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL TRAINING"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>>>>")
    trainer = ModelTrainingPipeline()
    trainer.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} finished <<<<<<<<\n===============================")
except Exception as e: 
    logger.exception(e)
    raise e