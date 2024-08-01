import os
from textSum.logging import logger
from textSum.config.configuration import ConfigurationManager
from textSum.components.model_trainer import ModelTrainer 

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()
        trainer = ModelTrainer(config=trainer_config)
        trainer.train()