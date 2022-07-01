from objects.game_object import GameObject
from settlers_of_valgard.colors import WOOD

class Resource(GameObject):
    class Schema(GameObject.Schema):
        is_static = True
        numeric_id = False
    
    def __init__(self, name, color) -> None:
        self.name = name
        self.id = name
        self.color = color

        super().__init__()

Wood = Resource('Wood', WOOD)