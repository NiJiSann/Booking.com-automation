import random
from dataclasses import dataclass


@dataclass
class CarRentalData:
    age: str = str(random.randint(18, 99))
    pic_up_location: str = "Dubai"
    drop_off_location: str = "Burj Khalifa"
    pick_up_date: str = "20 May"
    drop_off_date: str = "30 May"
    pick_up_time: str = "06:00"
    drop_off_time: str = "06:00"


