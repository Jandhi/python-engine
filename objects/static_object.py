from objects.game_object import GameObject

class StaticObject(GameObject):
    type = '__static_object'

    class Schema(GameObject.Schema):
        is_static = True
        numeric_id = False
    
    def __init__(self, id) -> None:
        self.id = id
        super().__init__()