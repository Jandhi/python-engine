from objects.node import Node

# z levels
# 0 - ground
# 3 - floor
# 6 - items
# 10 - settlers

class MapEntity(Node):
    def __init__(self, is_collision, pos) -> None:
        super().__init__()
        self.is_collision = is_collision
        self.x, self.y, self.z = pos
    
    @property
    def pos(self):
        return self.x, self.y, self.z
    
    @pos.setter
    def pos(self, value):
        self.x, self.y, self.z = value
    
    def insert_into(self, map):
        map.tiles[self.x][self.y].entities.append(self)
    
    def remove_from(self, map):
        map.tiles[self.x][self.y].entities.remove(self)
    
    def move_to(self, map, x, y):
        self.remove_from(map)
        self.x = x
        self.y = y
        self.insert_into(map)