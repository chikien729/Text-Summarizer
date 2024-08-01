import os
from textSum.logging import logger
from textSum.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config
        
    def validate_all_files_exist(self):
        try:
            status = None
            all_folders = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            for folder in all_folders:
                if folder not in self.config.ALL_REQUIRED_FOLDERS:
                    status = False
                else: 
                    status = True
                with open(self.config.STATUS_FILE, "w") as file:
                    file.write(f"Validation_status: {status}")
            return status
        
        except Exception as e:
            raise e