from random import randint, choice
from pyfiglet import Figlet
import inquirer

from client.ansi import get_color_escape, set_color
from client.gradient import gradient
from utils.color import rgb_to_decimal
from templates.ideology import Ideology
from utils.json_reader import JSONLoader
from utils.tagify import tagify, detagify
from templates.vessel import Vessel
from client.clear import clear_screen

BOLD = '\033[1m'

f = Figlet(font='roman', width=200)

clear_screen()
print(gradient(
    "\n".join(f.renderText("IdeologyWars").split("\n")[:9]),
    rgb_to_decimal((250, 100, 75)),
    rgb_to_decimal((0, 255, 218)),
))

ideology_json = JSONLoader("data/ideologies.json").read()
pack_data = {}
ideology_data = {}

#* O(n^2) but it's not that bad.
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

x, y = 0, 0
vessel = Vessel()

while True:
    question = [
        inquirer.List('answer',
            message="What pack do you want to open?",
            choices=[tagify(pack) for pack in pack_data]
        )
    ]

    pack = detagify(inquirer.prompt(question)['answer'])
    clear_screen()

    if pack not in pack_data:
        print("\nInvalid pack.")
    elif pack == 'exit':
        print("\nExiting...")
        break
    else:
        ideology = choice(pack_data[pack])
        ideology_data[ideology].info()
        print()

        vessel.add_to_grid(ideology_data[ideology], x, y)
        vessel.grid_info()
        print()

        # Change x and y to the next available space.
        if x != 2:
            x += 1
        else:
            x = 0
            y += 1