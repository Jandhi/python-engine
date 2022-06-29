from objects.game_object import GameObject, find_object, get_object_pool, initialize_objects
from objects.save_and_load import save_file, load_file

initialize_objects()

class Static(GameObject):
    class Schema(GameObject.Schema):
        is_static = True
        numeric_id = False
    
    def __init__(self, name) -> None:
        self.name = name
        self.id = name
        
        super().__init__()

class NonStatic(GameObject):
    class Schema(GameObject.Schema):
        numeric_id = False

    def __init__(self, name, pointer) -> None:
        self.name = name
        self.id = name
        self.pointer = pointer
        
        super().__init__()

test = Static("test")
test2 = NonStatic("test2", test)

save_file('tests/output/static_objects')

assert(not "test" in get_object_pool())

load_file('tests/output/static_objects')

assert(find_object(Static, "test") is not None)
assert(find_object(NonStatic, "test2").pointer is not None)