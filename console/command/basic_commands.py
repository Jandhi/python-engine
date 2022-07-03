from console.command.command import Command
from game import set_running

def Quit(cmd):
    set_running(False)
    print("Goodbye!")

Command(
    "Quit",
    "Quits the game",
    Quit,
    ['q', 'quit', 'exit', 'end'],
)