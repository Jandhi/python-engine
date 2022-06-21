from console.console import cprint
from objects.game_object import GameObject, initialize_objects

initialize_objects()

class Test(GameObject):
    color = 'red'

    def __init__(self) -> None:
        super().__init__()

cprint(Test())