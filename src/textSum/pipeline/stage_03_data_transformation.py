import os
from textSum.logging import logger
from textSum.config.configuration import ConfigurationManager
from textSum.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_trans_config = config.get_data_transformation_config()
        data_trans = DataTransformation(config=data_trans_config)
        data_trans.convert()