from unicodedata import name
from noise.choose import choose
from settlers_of_valgard.colors import Colors
from console.colored_object import ColoredObject, name_table
from objects.static_object import StaticObject
from noise.seed import seed
from settlers_of_valgard.map.map_entity import MapEntity

class TilePrototype(StaticObject):
    def __init__(self, name, id, letters, colors) -> None:
        super().__init__(id=id)
        self.letters = letters
        self.name = name
        self.colors = colors

    def letter_at(self, x, y) -> str:
        return choose(seed() * x * y * 3, self.letters)

    def color_at(self, x, y) -> int:
        return choose(seed() * x * y, self.colors) 

Empty = TilePrototype('Empty', 0, ['.', '.', ','], [Colors.LEMON, Colors.OCEAN, Colors.GRASS])

class Tile(ColoredObject):
    def __init__(self, prototype : TilePrototype, x, y):
        self.prototype = prototype or Empty
        self.x = x 
        self.y = y
        self.entities : list[MapEntity] = []
    
    def __serialize_field__(self):
        return self.prototype.id

    def get_top_entity(self) -> MapEntity:
        entity = self.entities[0]

        for e in self.entities[1:]:
            if e.z > entity.z:
                entity = e
        
        return entity

    def get_title(self) -> str:
        if len(self.entities) > 0:
            return self.get_top_entity().get_symbol(self)

        return self.prototype.letter_at(self.x, self.y)
    
    def get_color(self) -> int:
        if len(self.entities) > 0:
            return self.get_top_entity().get_color(self)

        return self.prototype.color_at(self.x, self.y)