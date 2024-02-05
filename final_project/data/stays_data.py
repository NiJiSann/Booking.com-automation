from faker import Faker
import random


class StaysData:
    def __init__(self):
        self.fake = Faker()
        self.stay_destinations = ['Tashkent', 'Tbilisi', 'Samarkand', 'Dubai']
        self.stay_durations = ['1 day', '2 days', '3 days', '4 days']

    def get_stay_destination(self):
        return random.choice(self.stay_destinations)

    def get_stay_duration(self):
        return random.choice(self.stay_durations)
