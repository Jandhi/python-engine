from console.command.command import Command
from console.verification import get_verification
from game import set_running

def Quit(cmd):
    if get_verification("Do you really want to exit the game?"):
        set_running(False)
        print("Goodbye!")

Command(
    "Quit",
    "Quits the game",
    Quit,
    ['q', 'quit', 'exit', 'end'],
)