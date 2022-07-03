from mimetypes import init
from console.command.command_manager import CommandManager
from game import is_running

command_manager = CommandManager()

def start():
    main_loop()

def main_loop():
    import console.command.basic_commands

    while is_running():
        player_input = input("Please enter a command:\n")
        command_manager.process_input(player_input)

start()