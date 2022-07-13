from noise.dice import DicePool
from objects.enums.enum import NamedEnum, OrderedEnum
from objects.static_object import StaticObject
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.events.event import BlockableEvent, SoVEvent

class Skill(NamedEnum):
    def __init__(self, name, color) -> None:
        super().__init__(name, color)



class SkillLevel(OrderedEnum):
    def __init__(self, name, color, value, xp_threshold) -> None:
        super().__init__(name, color, value)
        self.xp_threshold = xp_threshold
    
    def get_dice(self):
        return SKILL_DICE[self.value]

Unskilled = SkillLevel("Unskilled", Colors.STONE, 0, 0) #1d4
Novice = SkillLevel("Novice", Colors.GRASS, 1, 5)       #2d4
Apprentice = SkillLevel("Apprentice", Colors.SKY, 2, 15) #3d4
# regular workers should get to these tiers in time
Competent = SkillLevel("Competent", Colors.ORANGE, 3, 30) #1d6, 1d4
Skilled = SkillLevel("Skilled", Colors.LAKE, 4, 60)       #2d6
Adept = SkillLevel("Adept", Colors.CRIMSON, 5, 120)        #3d6
# highest tier, only few should make it this far
Expert = SkillLevel("Expert", Colors.MAGENTA, 6, 200)      #2d8
Master = SkillLevel("Master", Colors.GOLD, 7, 400)         #3d8

LEVELS = [Unskilled, Novice, Apprentice, Competent, Adept, Expert, Master]
SKILL_DICE = {
    0 : DicePool((1, 4)), 
    1 : DicePool((2, 4)), 
    2 : DicePool((3, 4)), 
    3 : DicePool((1, 4), (1, 6)), 
    4 : DicePool((2, 6)),
    5 : DicePool((3, 6)),
    6 : DicePool((2, 8)),
    7 : DicePool((3, 8)),
}

ODDS = {
    0 : [0.25,  0.25,   0.25,  0.25,     0,     0,     0,     0],
    1 : [0.063, 0.188, 0.313, 0.438,     0,     0,     0,     0],
    2 : [0.016, 0.109, 0.297, 0.578,     0,     0,     0,     0],
    3 : [0.042, 0.125, 0.208, 0.292, 0.167, 0.167,     0,     0],
    4 : [0.028, 0.083, 0.139, 0.194,  0.25, 0.306,     0,     0],
    5 : [0.046, 0.032, 0.088, 0.171, 0.282, 0.421,     0,     0],
    6 : [0.016, 0.047, 0.078, 0.109, 0.141, 0.172, 0.203, 0.234],
    7 : [0.002, 0.012, 0.037, 0.072, 0.119, 0.178, 0.248, 0.330],
}

def get_level(xp):
    for skill in LEVELS[::-1]:
        if xp >= skill.xp_threshold:
            return skill
    
    return Unskilled

class AddXPEvent(BlockableEvent):
    def __init__(self, settler, skill, amt) -> None:
        super().__init__()
        self.settler = settler
        self.skill = skill
        self.amount = amt

class LevelUpEvent(SoVEvent):
    def __init__(self, settler, skill, old_level, new_level) -> None:
        super().__init__()
        self.settler = settler
        self.skill = skill
        self.old_level = old_level
        self.new_level = new_level

class LevelDownEvent(SoVEvent):
    def __init__(self, settler, skill, old_level, new_level) -> None:
        super().__init__()
        self.settler = settler
        self.skill = skill
        self.old_level = old_level
        self.new_level = new_level