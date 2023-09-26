from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME_01 = "Data Ingestion stage"

try: 
    logger.info(f">>>>> stage {STAGE_NAME_01} started <<<<<<<<<")

    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(f">>>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx===============x")

except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME_02 = "Data Validation Stage"

try: 
    logger.info(f">>>>>> stage {STAGE_NAME_02} started <<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()

    logger.info(f">>>>> stage {STAGE_NAME_02} completed <<<<<<\n\nx===============x")

except Exception as e:
    logger.exception(e)
    raise e 