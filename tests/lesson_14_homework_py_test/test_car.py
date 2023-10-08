from car import Car
import pytest
import random
from faker import Faker


class TestCar:

    def setup_method(self):
        fake = Faker()
        self.new_car = Car(fake.vehicle_make(), fake.vehicle_model(), random.randint(0, 100000))
        print(fake.vehicle_make(), fake.vehicle_model())

    def test_start_stopped_engine(self):
        assert self.new_car.start_engine() == "Engine started."

