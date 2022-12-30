from car import Serviceable

class Engine(Serviceable):
    def __init__(self) -> None:
        self.current_mileage = 0
        self.last_service_mileage = 0

    def set_current_mileage(self, mileage):
        self.current_mileage = mileage
    
    def set_last_service_mileage(self, mileage):
        self.last_service_mileage = mileage


class CapuletEngine(Engine):
    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True

class WilloughbyEngine(Engine):
    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 60000:
            return True

class SternmanEngine(Engine):
    def __init__(self) -> None:
        self.warning_light = False

    def set_warning_light(self, light):
        self.warning_light = light

    def needs_service(self):
        return self.warning_light