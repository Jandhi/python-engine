from objects.static_object import StaticObject
from settlers_of_valgard.map.map_entity import MapEntity

class TilePrototype(StaticObject):
    def __init__(self, name, letter) -> None:
        super().__init__(id=letter)
        self.letter = letter
        self.name = name

class Tile:
    def __init__(self, prototype : TilePrototype) -> None:
        self.entities : list[MapEntity] = []
        self.prototype = prototype
    
    def __serialize_field__(self):
        if self.prototype is None:
            return '0'
        else:
            return self.prototype.letter