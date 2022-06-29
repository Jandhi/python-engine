from objects.game_object import GameObject


class Building(GameObject):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.prototype = None