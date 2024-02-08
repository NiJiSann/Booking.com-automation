import random
from dataclasses import dataclass


@dataclass
class CarRentalData:
    age: str = str(random.randint(18, 99))
    pic_up_location: str = "Dubai"
    drop_off_location: str = "Burj Khalifa"
    pick_up_date: str = "25 May"
    drop_off_date: str = "30 May"
    pick_up_time: str = random.choice(["08:00", "09:30", "10:30", "04:30"])
    drop_off_time: str = random.choice(["12:00", "12:30", "15:30", "18:30"])


