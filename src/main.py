from random import randint, choice
from pyfiglet import Figlet
import inquirer

from console.ansi import get_color_escape, set_color
from console.gradient import gradient
from utils.color import rgb_to_decimal
from templates.ideology import Ideology
from utils.json_reader import JSONLoader
from utils.tagify import tagify, detagify
from templates.player import Player
from console.clear import clear_screen

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
        try:
            ideology = choice(pack_data[pack])
            ideology_data[ideology].info()
            print()

            player = Player()
            player.vessels[0].add_cards([ideology_data[ideology]])
            player.vessels[0].info()
            print()
        except ValueError:
            print("\nNo ideologies in this pack can be utilized.")