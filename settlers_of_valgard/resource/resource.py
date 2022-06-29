from objects.game_object import GameObject

class Resource(GameObject):
    class Schema(GameObject.Schema):
        is_static = True
        numeric_id = False
    
    def __init__(self, name, color) -> None:
        self.name = name
        self.id = name
        self.color = color

        super().__init__()

wood = Resource('Wood', 'orange_4b')