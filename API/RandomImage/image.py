import os
import shutil
from pathlib import Path
import requests


class Image:
    @staticmethod
    def download(name: str, width: int, height: int) -> str:
        """" Downloads and returns path to image"""
        api_key = 'dFXrkFkg51ChfqaFGngjPQ==8fLvtI7Atv8eXyj1'
        api_url = 'https://api.api-ninjas.com/v1/randomimage?'
        headers = {
            'X-Api-Key': api_key,
            'Accept': 'image/jpg'
        }
        params = {
            'category': 'abstract',
            'width': width,
            'height': height
        }
        response = requests.get(api_url, headers=headers, params=params, stream=True)
        if response.status_code == requests.codes.ok:
            with open(name, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        else:
            print("Error:", response.status_code, response.text)

        path = os.path.join(Path.cwd(), name)
        return path
