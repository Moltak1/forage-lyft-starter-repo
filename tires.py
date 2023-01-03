from serviceable import Serviceable

class Tires(Serviceable):
    def __init__(self, wear) -> None:
        self.wear = wear

    def needs_service(self):
        pass

class CarriganTires(Tires):
    def needs_service(self):
        for tire in self.wear:
            if tire >= 0.9:
                return True
        return  False

class OctoprimeTires(Tires):
    def needs_service(self):
        if sum(self.wear) >= 3:
            return True
        return False