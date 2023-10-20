from tires.tires import Tires


class OctoprimeTire(Tires):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_to_service = 3.0

    def need_service(self):
        if sum(self.tire_wear) >= self.tire_need_to_service:
            return True
        return False    