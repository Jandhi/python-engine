from objects.game_object import find_object
from objects.static_object import StaticSingleton
from settlers_of_valgard.tech.technology import DISCOVERED, LOCKED, UNLOCKED, TechDiscoveredEvent, Technology
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.player_info import PlayerInfo
from objects.query import Query
from events.game_event import add_listener

class TechManager(StaticSingleton):
    instance = None

    def __init__(self) -> None:
        super().__init__()

        self.settlement : Settlement = None
        self.player_info : PlayerInfo = None
        TechManager.instance = self
    
    def __get_status(self, tech : Technology):
        if tech in self.settlement.discovered_technologies:
            return DISCOVERED
        
        if tech.required_rank < self.player_info.rank:
            return LOCKED
        
        for other in tech.required_tech:
            if other not in self.settlement.discovered_technologies:
                return LOCKED
        
        return UNLOCKED

    def update(self):
        self.settlement = find_object(Settlement)
        self.player_info = find_object(PlayerInfo)

        for tech in Query(Technology).all():
            tech.status = self.__get_status(tech)

add_listener(TechDiscoveredEvent, lambda tech : TechManager.instance.update())