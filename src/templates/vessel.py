from pyfiglet import Figlet

from .ideology import Ideology
from console.ansi import get_color_escape, set_color
from utils.categorize import al, lr

class Vessel:
    def __init__(self, cards=[]) -> None:
        self.cards = cards
        self.stats = {
            'lr': 0,
            'al': 0,
        }

    def json(self):
        cards = [card.name for card in self.cards]

        return {
            'cards': cards,
            'stats': self.stats
        }

    #? Maybe return self?
    def add_cards(self, cards):
        for card in cards:
            if not isinstance(card, Ideology):
                raise TypeError('Vessel can only hold Cards')
            if card in self.cards:
                raise ValueError('Cards cannot be duplicated')
            
            self.cards.append(card)
            self.stats['lr'] += card.lr
            self.stats['al'] += card.al

    def remove_cards(self, cards):
        for card in cards:
            if not isinstance(card, Ideology):
                raise TypeError('Vessel can only hold Cards')
                
            if card in self.cards:
                self.cards.remove(card)
                self.stats['lr'] -= card.lr
                self.stats['al'] -= card.al
            else:
                raise ValueError("Card doesn't exist")

    def info(self):
        darkblue = get_color_escape(0, 0, 175)
        yellow = get_color_escape(255, 255, 0)
        red = get_color_escape(255, 0, 0)
        blue = get_color_escape(0, 0, 255)
        BOLD = '\033[1m'

        f = Figlet(font='roman')
        print(set_color("\n".join(f.renderText("Vessel").split("\n")[:7]), blue))

        print(f"\n{set_color(BOLD + 'Authoritarian', darkblue)}-{set_color(BOLD + 'Libertarian', yellow)}: " + al(self.stats['al']))
        print(f"{set_color(BOLD + 'Left', red)}-{set_color(BOLD + 'Right', blue)}: " + lr(self.stats['lr']))