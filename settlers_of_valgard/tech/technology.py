from objects.enums.enum import OrderedEnum
from objects.game_object import find_object
from objects.query import Query
from objects.static_object import StaticObject, StaticSingleton
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.rank import Freeman
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.player_info import PlayerInfo
from events.game_event import GameEvent, add_listener

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
    
    def discover(self):
        settlement : Settlement = find_object(Settlement)
        settlement.discovered_technologies.append(self)
        # TODO
        TechDiscoveredEvent(self).send()

class TechDiscoveredEvent(GameEvent):
    def __init__(self, tech) -> None:
        super().__init__()
        self.tech = tech