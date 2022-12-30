from datetime import datetime
from car import Serviceable


class Battery(Serviceable):
    def __init__(self) -> None:
        self.last_service_date = datetime.today().date()
    
    def set_last_service_date(self, date:datetime):
        self.last_service_date = date

class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()

class NubbinBattery(Battery):
    def needs_service(self) -> bool:
        return self.last_service_date.replace(year=self.last_service_date.year + 4) < datetime.today().date()