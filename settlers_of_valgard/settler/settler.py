from objects.game_object import GameObject

class Settler(GameObject):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.family = None
        self.workplace = None