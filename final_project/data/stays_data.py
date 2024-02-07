from faker import Faker
import random


class StaysData:
    def __init__(self):
        self.fake = Faker()
        self.stay_durations = ['1 day', '2 days', '3 days', '7 days']
    
    @staticmethod
    def get_stay_destinations():
        return ['Tashkent', 'Tbilisi', 'Samarkand', 'Dubai']

    @staticmethod
    def get_stay_destination():
        return random.choice(['Tashkent', 'Tbilisi', 'Samarkand', 'Dubai'])

    def get_stay_duration(self):
        return random.choice(self.stay_durations)
