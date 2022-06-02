from pyfiglet import Figlet
from prettytable.colortable import ColorTable, Theme

from .ideology import Ideology
from client.ansi import get_color_escape, set_color
from utils.categorize import al, lr
from utils.nth_repl import nth_repl

class Vessel:
    def __init__(self, grid=None) -> None:
        self.stats = {
            'lr': 0,
            'al': 0,
        }

        if grid is None:
            self.grid = [[None for x in range(3)] for y in range(3)]
        else:
            self.grid = grid

    def json(self):
        grid = [card.name for card in self.grid]

        return {
            'grid': grid,
            'stats': self.stats
        }

    def add_to_grid(self, card, x, y):        
        if not isinstance(card, Ideology):
            raise TypeError('Grid can only hold cards')

        try:
            if self.grid[y][x] is not None:
                raise ValueError('Position already occupied')
        except IndexError:
            raise ValueError('Grid is full')
        
        self.grid[y][x] = card
        self.stats['lr'] += card.lr
        self.stats['al'] += card.al

        return True

    def remove_from_grid(self, card):
        if not isinstance(card, Ideology):
            raise TypeError('Grid can only hold cards')

        for level in self.grid:
            for _card in level:
                if _card is not None:
                    if _card.name == card.name:
                        self.stats['lr'] -= _card.lr
                        self.stats['al'] -= _card.al
                        _card = None
                        return True

        raise ValueError('Card not found')

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
    
    def grid_info(self):
        BASED = Theme(
            default_color="91",
            vertical_color="91",
            horizontal_color="91",
            junction_color="91",
        )

        table = ColorTable(["╲"] + [str(x) for x in range(len(self.grid[0]))], theme=BASED)

        for y in range(len(self.grid)):
            table.add_row([str(y)] + ["\033[1m" + card.name + "\033[m" if card is not None else "..." for card in self.grid[y]])

        table = table.get_string().replace("|", "│").replace("-", "─").split("\n")

        table[0] = nth_repl(table[0], "+", "╭", 1)
        table[0] = nth_repl(table[0], "+", "╮", len(self.grid[0]) + 1)
        table[0] = table[0].replace("+", "┬")

        table[-1] = nth_repl(table[-1], "+", "╰", 1)
        table[-1] = nth_repl(table[-1], "+", "╯", len(self.grid[0]) + 1)
        table[-1] = table[-1].replace("+", "┴")

        for i in range(1, len(table) - 1):
            table[i] = nth_repl(table[i], "+", "├", 1)
            table[i] = nth_repl(table[i], "+", "┤", len(self.grid[0]) + 1)
            table[i] = table[i].replace("+", "┼")

        table = "\n".join(table)
        print(table)