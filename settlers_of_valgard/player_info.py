from objects.singleton import Singleton
from settlers_of_valgard.logger.logging_level import Normal
from settlers_of_valgard.rank import Freeman

class PlayerInfo(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.rank = Freeman
        self.logging_level = Normal