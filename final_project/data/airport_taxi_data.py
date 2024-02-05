import random
from dataclasses import dataclass
from faker import Faker
faker = Faker()


@dataclass
class AirportTaxiDate:
    pic_up_location: str = "Dubai"
    destination_location: str = "Burj Khalifa"
    pick_up_date: str = "20 April"
    pick_up_time: str = "15:30"
    passenger_count: str = str(random.randint(1, 5))


@dataclass
class AirportTaxiDetailsDate:
    comment: str = faker.text()

