from objects.node import Node

# z levels
# 0 - ground
# 3 - floor
# 6 - items
# 10 - settlers

class MapEntity(Node):
    def __init__(self, is_collision, pos, symbol, color) -> None:
        super().__init__()
        self.is_collision = is_collision
        self.x, self.y, self.z = pos
        self.symbol = symbol
        self.color = color
        self.map = None
    
    @property
    def pos(self):
        return self.x, self.y, self.z
    
    @pos.setter
    def pos(self, value):
        self.x, self.y, self.z = value

    @property
    def tile(self):
        return self.map.tiles[self.x][self.y]

    def load_into(self, map):
        self.map = map
        self.insert_into(map)
    
    def insert_into(self, map):
        self.tile.entities.append(self)
    
    def remove_from(self, map):
        self.tile.entities.remove(self)
    
    def move_to(self, map, x, y):
        self.remove_from(map)
        self.x = x
        self.y = y
        self.insert_into(map)
    
    def get_symbol(self, tile):
        return self.symbol
    
    def get_color(self, tile):
        return self.color