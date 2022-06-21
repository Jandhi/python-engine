from objects.game_object import GameObject, find_object, initialize_objects
from objects.save_and_load import load_file, save_file
from colored import fg, attr

initialize_objects()

class Quest(GameObject):
    def __init__(self, name, color) -> None:
        super().__init__()

        self.name = name
        self.color = color

j = Quest('Finding the Godsword', 'red')

save_file('test')
load_file('test')

j = find_object(Quest, 0)

assert(f'{j} is my quest' == f'{fg("red")}Finding the Godsword{attr(0)} is my quest')