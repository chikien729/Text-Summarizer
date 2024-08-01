import os
from textSum.logging import logger
from textSum.config.configuration import ConfigurationManager
from textSum.components.model_evaluation import ModelEvaluation

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()