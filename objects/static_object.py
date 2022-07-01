from objects.game_object import GameObject, get_static_pool

class StaticObject(GameObject):
    type = '__static_object'

    class Schema(GameObject.Schema):
        is_static = True
        numeric_id = False
    
    def __init__(self, id) -> None:
        self.id = id
        super().__init__()

def list_statics():
    pool = get_static_pool()

    for type in pool:
        s = f'{type}: '
        
        for val in pool[type].values():
            s = f'{s} {val}'
        
        print(s)