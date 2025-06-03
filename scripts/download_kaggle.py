import os

from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi


def download_data(dataset_name):
    load_dotenv()

    os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

    api = KaggleApi()
    api.authenticate()

    output_dir = 'data'

    api.dataset_download_files(dataset_name, path=output_dir, unzip=True)

    print(f"Dataset downloaded to: {output_dir}")
