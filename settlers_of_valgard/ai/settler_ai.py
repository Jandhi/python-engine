from objects.node import Node
from settlers_of_valgard.ai.ai_node import AI
from settlers_of_valgard.map.map_entity import MapEntity
from noise.choose import choose
from noise.seed import seed

class SettlerAI(AI):
    def __init__(self) -> None:
        super().__init__()
        self.map_entity : MapEntity = None

    def on_added(self, parent : Node) -> None:
        self.map_entity = parent.get_child(MapEntity)
    
    def on_removed(self, parent) -> None:
        self.map_entity = None
    
    def on_act(self, ticknum):
        if self.map_entity is None:
            return
        
        x, y, z = self.map_entity.pos

        dirs = []

        if x > 0:
            dirs.append((-1, 0, 0))
        if x < self.map_entity.map.width - 1:
            dirs.append((1, 0, 0))
        if y > 0:
            dirs.append((0, -1, 0))
        if y < self.map_entity.map.height - 1:
            dirs.append((0, 1, 0))

        if len(dirs) == 0:
            return
        
        dx, dy, dz = choose(seed() * self.id * ticknum, dirs)
        self.map_entity.move_to(self.map_entity.map, x + dx, y + dy)

        self.cooldown += 4