import unittest
from .. import battery
from datetime import  datetime

class TestSpindler(unittest.TestCase):
    def test_should_be_serviced(self):
        date = datetime.today()
        date = date.replace(year=date.year - 3)
        bat = battery.SpindlerBattery()
        bat.set_last_service_date(date)
        self.assertTrue(bat.needs_service())


    def test_should_not_be_serviced(self):
        date = datetime.today()
        date = date.replace(year=date.year - 1)
        bat = battery.SpindlerBattery()
        bat.set_last_service_date(date)
        self.assertFalse(bat.needs_service())


class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self):
        date = datetime.today()
        date = date.replace(year=date.year - 4)
        bat = battery.NubbinBattery()
        bat.set_last_service_date(date)
        self.assertTrue(bat.needs_service())

    def test_should_not_be_serviced(self):
        date = datetime.today()
        date = date.replace(year=date.year - 2)
        bat = battery.NubbinBattery()
        bat.set_last_service_date(date)
        self.assertFalse(bat.needs_service())


if __name__ == '__main__':
    unittest.main()
