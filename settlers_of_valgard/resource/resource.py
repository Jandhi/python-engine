from objects.game_object import GameObject
from objects.static_object import StaticObject
from settlers_of_valgard.colors import Colors

class Resource(StaticObject):
    def __init__(self, name, color) -> None:
        super().__init__(name)
        self.name = name
        self.color = color

Wood = Resource('Wood', Colors.WOOD)