from objects.game_object import GameObject

class BuildingPrototype(GameObject):
    def __init__(self, name) -> None:
        super().__init__()
        
        self.name = name