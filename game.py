from mimetypes import init
from console.choice import choice
from console.command.command_manager import CommandManager
from engine_settings import EngineSettings
from objects.game_object import find_object

command_manager = CommandManager()
engine_settings = find_object(EngineSettings)

def start():
    main_loop()

def main_loop():
    import console.command.basic_commands
    import settlers_of_valgard.settlers_of_valgard

    while engine_settings.is_running():
        player_input = input("Please enter a command:\n")
        command_manager.process_input(player_input)

start()