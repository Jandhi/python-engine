from console.colored_string import color
from console.command.command_manager import CommandManager
from console.error import print_error
from console.palette import Palette
from objects.game_object import find_object

def choice(question, options = None, named_options = None):
    options = options or []
    named_options = named_options or {}

    while True:
        print(question)

        for index, (item, description) in enumerate(options):
            num = color(str(index + 1), Palette.INPUT_COLOR)
            print(f"{num}: {description}")

        for name, (item, description) in named_options.items():
            name = color(name, Palette.INPUT_COLOR)
            print(f"{name}: {description}")

        s = input()

        try:
            val = int(s)

            if 1 <= val <= len(options):
                return options[val - 1][0]
            
            print_error("Value is out of range.")

        except ValueError:
            if input.lower() in named_options:
                return named_options[name]
            else:
                find_object(CommandManager).process_input(s) 