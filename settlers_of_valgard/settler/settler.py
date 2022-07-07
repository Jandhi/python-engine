from objects.game_object import GameObject
from settlers_of_valgard.settler.skill import SkillLevel, Unskilled, get_level
from settlers_of_valgard.colors import Colors

class Settler(GameObject):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.color = Colors.GRASS
        self.family = None
        self.workplace = None
        self.xp = {}
    
    def get_skill_level(self, skill) -> SkillLevel:
        return get_level(self.xp[skill])
    
    def add_xp(self, skill, amt):
        if skill not in self.xp:
            self.xp[skill] = 0
        
        self.xp[skill] += amt