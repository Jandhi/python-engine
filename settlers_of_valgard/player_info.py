from objects.singleton import Singleton
from settlers_of_valgard.rank import Freeman, RankChangeEvent

class PlayerInfo(Singleton):
    rank = Freeman

    def set_rank(self, rank):
        if PlayerInfo.rank != rank:
            RankChangeEvent(PlayerInfo.rank, rank).send()
            PlayerInfo.rank = rank