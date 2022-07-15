from console.command.command import Command
from console.verification import get_verification
from engine_settings import EngineSettings
from objects.game_object import find_object

def Quit(cmd):
    if get_verification("Do you really want to exit the game?"):
        find_object(EngineSettings).set_running(False)
        print("Goodbye!")

Command(
    "Quit",
    "Quits the game",
    Quit,
    ['q', 'quit', 'exit', 'end'],
)