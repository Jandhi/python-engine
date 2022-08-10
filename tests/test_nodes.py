from objects.game_object import find_object, initialize_objects
from objects.save_and_load import load_file, save_file


initialize_objects()

from objects.node import Node

class Thing(Node):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name


a = Thing('a')
b = Thing('b')

a_id = a.id
b_id = b.id

a.add_child(b)

save_file('tests/output/nodes')
load_file('tests/output/nodes')

assert(find_object(Thing, a_id) is not None)
assert(find_object(Thing, b_id) is not None)
assert(a.get_child(Thing) is not None)
assert(b.parent is a)