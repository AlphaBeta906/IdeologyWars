from locale import currency


class Player:
    def __init__(self, vessels:int=5, inventory:list=[], currency:int=100) -> None:
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
            self.vessels += amount
            self.currency -= price