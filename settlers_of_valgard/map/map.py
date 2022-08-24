from .map_entity import MapEntity
from .tile import Tile, TilePrototype
from objects.game_object import GameObject, find_object
from objects.query import Query

class Map(GameObject):

    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.tiles = [[Tile(None, x, y) for x in range(height)] for y in range(width)]
        load_entities(self)
    
    # tiles is converted from string to tiles
    # called at link step
    def __link__(self) -> None:
        for x in range(int(self.width)):
            for y in range(int(self.height)):
                self.tiles[x][y] = Tile(find_object(TilePrototype, int(self.tiles[x][y])), x, y)

        load_entities(self)

def load_entities(map : Map):
    for e in Query(MapEntity).all():
        e.load_into(map)