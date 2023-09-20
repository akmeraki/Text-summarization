import os 
import urllib.request as request
import gdown
import zipfile
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.utils.common import get_size


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):

        if not os.path.exists(self.config.local_data_file):

            filename, headers = request.urlretrieve(
            url = self.config.source_URL,
            filename= self.config.local_data_file
            )

            logger.info(f"{filename} download! with following info: \n {headers}")

        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")


    def google_drive_down(self):
        
        if not os.path.exists(self.config.local_data_file):

            prefix = 'https://drive.google.com/uc?/export=download&id='

            url = self.config.source_URL
            output = self.config.local_data_file
            
            file_id = url.split('/')[-2]

            gdown.download(prefix+file_id, output)

            logger.info(f"{output} download! with following info: \n")

        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")

        


    def extract_zip_file(self):

        """
        zip_file_path:str 
        Extracts the zip file into the data directory
        Function returns None 
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        