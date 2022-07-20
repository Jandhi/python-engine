from mimetypes import init
from console.choice import choice
from console.colored_string import color
from console.command.command_manager import CommandManager
from console.command.scopes import IN_GAME
from console.palette import Palette
from engine_settings import EngineSettings
from objects.game_object import find_object
from colored import attr

command_manager = CommandManager()
engine_settings = find_object(EngineSettings)

def start():
    main_loop()

def main_loop():
    import console.command.basic_commands
    import settlers_of_valgard.settlers_of_valgard
    command_manager.scopes.append(IN_GAME)

    while engine_settings.is_running():
        player_input = input(f'Please enter a command{attr(5)}..{attr(0)}\n')
        command_manager.process_input(player_input)
        print() # newline
start()