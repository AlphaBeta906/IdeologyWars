from .vessel import Vessel

class Player:
    def __init__(self, vessels:list=[Vessel() for x in range(5)], inventory:list=[], currency:int=100) -> None:
        self.vessels = vessels
        self.inventory = inventory,
        self.currency = currency

    def json(self) -> dict:
        return {
            'vessels': self.vessels,
            'inventory': self.inventory,
            'currency': self.currency
        }

    def add_vessels(self, amount:int) -> None:
        if amount > 0 and (price := amount) * 10 <= self.currency:
            for x in range(amount):
                self.vessels.append(Vessel())
                self.currency -= price