from objects.game_object import GameObject
from settlers_of_valgard.settler.skill import SkillLevel, Unskilled

class Settler(GameObject):
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.family = None
        self.workplace = None   
    
    def get_skill_level(self, skill) -> SkillLevel:
        return Unskilled