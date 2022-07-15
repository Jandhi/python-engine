from objects.game_object import GameObject

def make_instance(cls):
    return cls.__new__(cls)

class Singleton(GameObject):
    type = '__singleton'
    make_instance = make_instance

    class Schema(GameObject.Schema):
        is_singleton = True
    
