from objects.game_object import GameObject, initialize_objects
from objects.construction import add_constructor
from objects.save_and_load import load_file, save_file

initialize_objects()

class Obj(GameObject):
    def __init__(self) -> None:
        super().__init__()

        self.test = Test('jan')

class Test:
    type = 'test'

    def __init__(self, name) -> None:
        self.name = name

    def __serialize__(self):
        return {'type' : self.type, 'data' : self.name}

def make_test(data):
    return Test(data['data'])

add_constructor(Test.type, make_test)

obj = Obj()

obj.test = Test('nicole')

save_file('tests/output/serializeable')
load_file('tests/output/serializeable')

assert(obj.test.name == 'nicole')