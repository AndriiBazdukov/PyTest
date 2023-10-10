from car import Car
import pytest
import random


class TestCar:

    def setup_method(self):
        self.new_car = Car("Audi", "Q7", random.randint(0, 100000))

    def test_start_stopped_engine(self):
        assert self.new_car.start_engine() == "Engine started."

    def test_start_started_engine(self):
        self.new_car.start_engine()
        assert self.new_car.start_engine() == "Engine is already running."

    def test_stop_stopped_engine(self):
        assert self.new_car.stop_engine() == "Engine is already off."

    def test_stop_started_engine(self):
        self.new_car.start_engine()
        assert self.new_car.stop_engine() == "Engine stopped."

    def test_drive_with_stopped_engine(self):
        assert self.new_car.drive(random.randint(0, 100000)) == "Cannot drive. Engine is off."

    def test_exceeding_driving_limit(self):
        self.new_car.start_engine()
        assert self.new_car.drive(self.new_car.miles_limit + 1) == "The miles limit has been exceeded"

    def test_driving_no_exceeding_limit(self):
        self.new_car.start_engine()
        random_int_under_limit = random.randint(0, self.new_car.miles_limit)
        miles_to_drive = self.new_car.miles_limit - random_int_under_limit
        assert self.new_car.drive(miles_to_drive) == f"Driving {miles_to_drive} miles."

    def test_limit_change_when_driving(self):
        self.new_car.start_engine()
        limit_left_before = self.new_car.miles_limit
        random_int_under_limit = random.randint(0, limit_left_before)
        driving_distance = limit_left_before - random_int_under_limit

        self.new_car.drive(driving_distance)
        assert self.new_car.miles_limit == limit_left_before - driving_distance

    def test_miles_limit_property(self):
        limit = random.randint(0, 1000)
        car = Car("Audi", "A6", limit)
        assert car.miles_limit == limit

    @pytest.mark.xfail(reason="Marked until Drive function is fixed")
    def test_miles_invalid_format_drive_function(self):
        with pytest.raises(TypeError, match='Distance must be int'):
            self.new_car.drive("asdf")

    # Еще можно добавить тесты на валидацию полей в конструктое нл вроде как уже 10 и методы покрыты
