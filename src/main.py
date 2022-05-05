from pyfiglet import Figlet

from console.ansi import get_color_escape, set_color
from console.gradient import gradient
from utils.color import rgb_to_decimal
from templates.ideology import Ideology
from utils.json_reader import JSONLoader

BOLD = '\033[1m'

f = Figlet(font='slant')

print(gradient(
    f.renderText("IdeologyWars"),
    rgb_to_decimal((225, 0, 0)),
    rgb_to_decimal((0, 0, 225)),
))

ideology_json = JSONLoader("data/ideologies.json").read()
pack_data = {}
ideology_data = {}

#! O(n^2 + n) yuck!
for ideology in ideology_json:
    ideology_data[ideology] = Ideology(
        name=ideology_json[ideology]['name'].replace('\\033[', '\033['),
        description=ideology_json[ideology]['description'],
        al=ideology_json[ideology]['al'],
        lr=ideology_json[ideology]['lr'],
        tags=ideology_json[ideology]['tags'],
        contradicts=ideology_json[ideology]['contradicts']
    )

    for pack in ideology_json[ideology]['tags']:
        if pack not in pack_data:
            pack_data[pack] = []

        pack_data[pack].append(ideology)

for ideology in ideology_data:
    ideology_data[ideology].info()