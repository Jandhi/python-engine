from events.game_event import GameEvent
from objects.node import Node
from settlers_of_valgard.settler.skill import LevelDownEvent, SkillLevel, get_level, AddXPEvent, LevelUpEvent
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.map.map_entity import MapEntity

class Settler(Node):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.color = Colors.GRASS
        self.family = None
        self.workplace = None
        self.xp = {}

        self.add_child(MapEntity(True, (0, 0, 0), '@', self.color))

        CreatedSettlerEvent(self).send()
    
    def get_skill_level(self, skill) -> SkillLevel:
        if skill not in self.xp:
            return get_level(0)

        return get_level(self.xp[skill])
    
    def add_xp(self, skill, amt):
        lvl = self.get_skill_level(skill)

        if AddXPEvent(self, skill, amt).send_is_success():
            if skill not in self.xp:
                self.xp[skill] = 0
            
            self.xp[skill] += amt

            new_lvl = self.get_skill_level(skill)

            if new_lvl > lvl:
                LevelUpEvent(self, skill, lvl, new_lvl).send()
            elif new_lvl < lvl:
                LevelDownEvent(self, skill, lvl, new_lvl).send()

class CreatedSettlerEvent(GameEvent):
    def __init__(self, settler) -> None:
        super().__init__()
        self.settler : Settler = settler