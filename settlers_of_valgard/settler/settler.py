from objects.game_object import GameObject
from settlers_of_valgard.settler.skill import SkillLevel, Unskilled
from settlers_of_valgard.colors import Colors

class Settler(GameObject):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.color = Colors.GRASS
        self.family = None
        self.workplace = None   
    
    def get_skill_level(self, skill) -> SkillLevel:
        return Unskilled