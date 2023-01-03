import unittest
from .. import engine


class TestCapulet(unittest.TestCase):


    def test_should_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        test_engine = engine.CapuletEngine()
        test_engine.set_last_service_mileage(last_service_mileage)
        test_engine.set_current_mileage(current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_should_not_service(self):
        current_mileage = 0
        last_service_mileage = 0
        test_engine = engine.CapuletEngine()
        test_engine.set_last_service_mileage(last_service_mileage)
        test_engine.set_current_mileage(current_mileage)
        self.assertFalse(test_engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_should_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        test_engine = engine.WilloughbyEngine()
        test_engine.set_last_service_mileage(last_service_mileage)
        test_engine.set_current_mileage(current_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_should_not_service(self):
        current_mileage = 0
        last_service_mileage = 0
        test_engine = engine.WilloughbyEngine()
        test_engine.set_last_service_mileage(last_service_mileage)
        test_engine.set_current_mileage(current_mileage)
        self.assertFalse(test_engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_should_service(self):
        light = True
        test_engine = engine.SternmanEngine()
        test_engine.set_warning_light(light)
        self.assertTrue(test_engine.needs_service())

    def test_should_not_service(self):
        light = False
        test_engine = engine.SternmanEngine()
        test_engine.set_warning_light(light)
        self.assertFalse(test_engine.needs_service())


if __name__ == '__main__':
    unittest.main()
