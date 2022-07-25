from objects.singleton import Singleton
from settlers_of_valgard.rank import Freeman, RankChangeEvent
from settlers_of_valgard.logger.logging_level import Normal

class PlayerInfo(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.rank = Freeman
        self.logging_level = Normal
    
    def set_rank(self, rank):
        if self.rank != rank:
            RankChangeEvent(self.rank, rank).send()
            self.rank = rank