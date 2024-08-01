from textSum.pipeline.stage_01_data_ingestion import DataIngestionPipeline
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