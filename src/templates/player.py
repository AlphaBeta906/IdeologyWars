from .vessel import Vessel

class Player:
    def __init__(self, vessels:list=None, inventory:list=None, currency:int=100) -> None:
        self.currency = currency

        if vessels is None:
            self.vessels = [Vessel() for x in range(5)]
        else:
            self.vessels = vessels

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

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