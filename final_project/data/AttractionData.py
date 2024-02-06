from dataclasses import dataclass


@dataclass
class AttractionData:
    attractions_list = [
        ('Tashkent', 'Tashkent City', 'Attraction is found'),
        ('Tokyo', 'Skytree', 'Attraction is found'),
        ('Tokyo', 'Tokyo Tower', 'Attraction is found'),
        ('Tokyo', 'Tashkent City', 'Attraction is not found')
    ]
