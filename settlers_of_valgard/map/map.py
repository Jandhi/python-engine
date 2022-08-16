from .map_entity import MapEntity
from .tile import Tile, TilePrototype
from objects.game_object import GameObject, find_object
from objects.query import Query

class Map(GameObject):

    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.tiles = [[Tile(None) for _ in range(height)] for _ in range(width)]
    
    # tiles is converted from string to tiles
    # called a link step
    def __link__(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[x][y] = Tile(find_object(TilePrototype, self.tiles[x][y]))

        load_entities(self)

def load_entities(map):
    for e in Query(MapEntity).all():
        e.load_into(map)