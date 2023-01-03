import unittest
from .. import tires

class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self):
        tire_wear = [0, 0.5, 0.9, 0]
        test_tires = tires.CarriganTires(tire_wear)
        self.assertTrue(test_tires.needs_service())

    def test_should_not_be_serviced(self):
        tire_wear = [0, 0.5, 0.8, 0]
        test_tires = tires.CarriganTires(tire_wear)
        self.assertFalse(test_tires.needs_service())

class TestOctoprime(unittest.TestCase):

    def test_should_be_serviced(self):
        tire_wear = [0.8, 0.8, 0.8, 0.8]
        test_tires = tires.OctoprimeTires(tire_wear)
        self.assertTrue(test_tires.needs_service())

    def test_should_not_be_serviced(self):
        tire_wear = [0, 0.4, 0.6, 0.6]
        test_tires = tires.OctoprimeTires(tire_wear)
        self.assertFalse(test_tires.needs_service())

if __name__ == "main":
    unittest.main()