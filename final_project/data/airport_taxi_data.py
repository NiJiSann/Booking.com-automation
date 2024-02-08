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


@dataclass
class UserData:
    first_name: str = faker.first_name()
    last_name: str = faker.last_name()
    email: str = faker.email()
    phone_code: str = "UZ-+998"
    phone_number: str = "99" + "".join([str(random.randint(0, 9)) for _ in range(7)])


@dataclass
class PaymentData:
    first_name: str = faker.first_name()
    card_number: str = "4002537426393261"
    card_type: str = "MasterCard"
    expiration_date: str = "12/24"
    cvc: str = "123"
