import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImageData:
    non_image_type_file = os.path.join(Path.cwd(), '__init__.py')
    image_size_list = [
        ('200', '200', 'This image is too small. Please try again with an image of at least 300 x 300 pixels.'),
        ('600', '600', 'Successfully uploaded')
    ]
