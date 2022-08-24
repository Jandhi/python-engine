from objects.game_object import GameObject, find_object, initialize_objects
from objects.save_and_load import load_file, save_file

initialize_objects()

class Obj(GameObject):
    def __init__(self, num) -> None:
        super().__init__()
        self.num = num

obj = Obj(1)
id = obj.id

save_file('tests/output/numbers')
load_file('tests/output/numbers')

obj = find_object(Obj, id)
assert(obj.num == 1)