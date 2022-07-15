from objects.singleton import Singleton
from settlers_of_valgard.resource.bundle import Bundle

class Settlement(Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.day = 0
        self.settlers = []
        self.buildings = []
        self.stockpile = Bundle()
        self.unlocked_blueprints = []
        self.discovered_technologies = []