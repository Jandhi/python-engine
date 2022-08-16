from settlers_of_valgard.map.map_entity import MapEntity

class FatMapEntity(MapEntity):
    def __init__(self, is_collision, pos, width, height) -> None:
        super().__init__(is_collision, pos)
        self.width = width
        self.height = height
    
    def insert_into(self, map):
        for dx in range(self.width):
            for dy in range(self.height):
                map.tiles[self.x + dx][self.y + dy].entities.append(self)

    def remove_from(self, map):
        for dx in range(self.width):
            for dy in range(self.height):
                map.tiles[self.x + dx][self.y + dy].entities.remove(self)