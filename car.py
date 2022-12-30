from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):

    def __init__(self, engine, battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        out = False
        out = out or self.engine.needs_service()
        out = out or self.battery.needs_service()
        return out


class CarFactory():

    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        car = Car()

    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        pass

    def create_palindrome(last_service_date, warning_light):
        pass

    def create_roschach(last_service_date, current_mileage, last_service_mileage):
        pass

    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        pass