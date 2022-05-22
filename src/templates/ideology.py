from console.ansi import get_color_escape, set_color
from utils.tagify import tagify
from utils.categorize import al, lr

darkblue = get_color_escape(0, 0, 175)
yellow = get_color_escape(255, 255, 0)
red = get_color_escape(255, 0, 0)
blue = get_color_escape(0, 0, 255)
BOLD = '\033[1m'

class Ideology:
    def __init__(self, name, description, al, lr, tags, contradicts) -> None:
        self.name = name
        self.description = description
        self.al = al
        self.lr = lr
        self.tags = tags
        self.contradicts = contradicts

    def info(self) -> None:
        #! This is a mess.
        print("\033[1m" + self.name + "\033[m")
        print("\n\"" + self.description + "\"")
        print(f"\n{set_color(BOLD + 'Authoritarian', darkblue)}-{set_color(BOLD + 'Libertarian', yellow)}: " + al(self.al))
        print(f"{set_color(BOLD + 'Left', red)}-{set_color(BOLD + 'Right', blue)}: " + lr(self.lr))
        print("Tags: " + ", ".join([tagify(tag) for tag in self.tags]))
        print("Contradicts: " + ", ".join([tagify(tag) for tag in self.contradicts]))

    def json(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'al': self.al,
            'lr': self.lr,
            'tags': self.tags,
            'contradicts': self.contradicts
        }