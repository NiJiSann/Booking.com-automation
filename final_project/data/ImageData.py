import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImageData:
    non_image_type_file = os.path.join(Path.cwd(), '/__init__.py')
    image_size_list = [
        ('200', '200', 'Something went wrong'),
        ('600', '600', 'Successfully uploaded')
    ]
