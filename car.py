from abc import ABC, abstractmethod
import engine, battery

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):

    def __init__(self, engine:engine.Engine, battery:battery.Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        out = False
        out = out or self.engine.needs_service()
        out = out or self.battery.needs_service()
        return out


class CarFactory():

    def create_calliope(last_service_date:battery.datetime, current_mileage:int, last_service_mileage:int) -> Car:
        en = engine.CapuletEngine()
        en.set_current_mileage(current_mileage)
        en.set_last_service_mileage(last_service_mileage)
        bat = battery.SpindlerBattery()
        bat.set_last_service_date(last_service_date)
        car = Car(en, bat)

    def create_glissade(last_service_date:battery.datetime, current_mileage:int, last_service_mileage:int) -> Car:
        en = engine.WilloughbyEngine()
        en.set_current_mileage(current_mileage)
        en.set_last_service_mileage(last_service_mileage)
        bat = battery.SpindlerBattery()
        bat.set_last_service_date(last_service_date)
        car = Car(en, bat)
        return car

    def create_palindrome(last_service_date:battery.datetime, warning_light: bool) -> Car:
        en = engine.SternmanEngine()
        en.set_warning_light(warning_light)
        bat = battery.SpindlerBattery()
        bat.set_last_service_date(last_service_date)
        car = Car(en, bat)
        return car

    def create_roschach(last_service_date:battery.datetime, current_mileage:int, last_service_mileage:int) -> Car:
        en = engine.WilloughbyEngine()
        en.set_current_mileage(current_mileage)
        en.set_last_service_mileage(last_service_mileage)
        bat = battery.NubbinBattery()
        bat.set_last_service_date(last_service_date)
        car = Car(en, bat)
        return car

    def create_thovex(last_service_date:battery.datetime, current_mileage:int, last_service_mileage:int) -> Car:
        en = engine.CapuletEngine()
        en.set_current_mileage(current_mileage)
        en.set_last_service_mileage(last_service_mileage)
        bat = battery.NubbinBattery()
        bat.set_last_service_date(last_service_date)
        car = Car(en, bat)
        return car