from mimetypes import init
from console.choice import choice
from console.command.command_manager import CommandManager
from game import is_running

command_manager = CommandManager()

def start():
    main_loop()

def main_loop():
    import console.command.basic_commands
    import settlers_of_valgard.settlers_of_valgard

    while is_running():
        player_input = input("Please enter a command:\n")
        command_manager.process_input(player_input)

start()