import unittest
from .. import car
from datetime import datetime


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 30001
        last_service_mileage = 0

        test_car = car.CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 30000
        last_service_mileage = 0

        test_car = car.CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 60001
        last_service_mileage = 0

        test_car = car.CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 60000
        last_service_mileage = 0

        test_car = car.CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        test_car = car.CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(test_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        test_car = car.CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(test_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        warning_light_is_on = True

        test_car = car.CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(test_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        warning_light_is_on = False

        test_car = car.CarFactory.create_palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(test_car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_roschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_roschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 60001
        last_service_mileage = 0

        test_car = car.CarFactory.create_roschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 60000
        last_service_mileage = 0

        test_car = car.CarFactory.create_roschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        test_car = car.CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 30001
        last_service_mileage = 0

        test_car = car.CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(test_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today()
        current_mileage = 30000
        last_service_mileage = 0

        test_car = car.CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(test_car.needs_service())


if __name__ == '__main__':
    unittest.main()
