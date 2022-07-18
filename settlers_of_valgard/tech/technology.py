from objects.enums.enum import OrderedEnum
from objects.game_object import find_object
from objects.query import Query
from objects.static_object import StaticObject, StaticSingleton
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.rank import Freeman
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.player_info import PlayerInfo

# tech status
class TechStatus(OrderedEnum):
    def __init__(self, name, color, value) -> None:
        super().__init__(name, color, value)

LOCKED = TechStatus('Locked', Colors.RED, 0)
UNLOCKED = TechStatus('Unlocked', Colors.SUNSHINE, 1)
DISCOVERED = TechStatus('Discovered', Colors.GRASS, 2)

class Technology(StaticObject):
    def __init__(self, name, color, required_tech = None, required_rank = Freeman) -> None:
        super().__init__(id = name)
        self.name = name
        self.color = color
        self.required_tech = required_tech or []
        self.required_rank = required_rank
        self.status = LOCKED

class TechManager(StaticSingleton):
    def __init__(self) -> None:
        super().__init__()

        self.settlement : Settlement = None
        self.player_info : PlayerInfo = None
    
    def __get_status(self, tech : Technology):
        if tech in self.settlement.discovered_technologies:
            return DISCOVERED
        
        if tech.required_rank < self.player_info.rank:
            return LOCKED
        
        for other in tech.required_tech:
            if other not in self.settlement.discovered_technologies:
                return LOCKED
        
        return UNLOCKED

    def update_status(self):
        self.settlement = find_object(Settlement)
        self.player_info = find_object(PlayerInfo)

        for tech in Query(Technology).all():
            tech.status = self.__get_status(tech)