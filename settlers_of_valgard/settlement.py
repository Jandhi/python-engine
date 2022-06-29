from objects.singleton import Singleton

class Settlement(Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.day = 0
        self.settlers = []
        self.buildings = []