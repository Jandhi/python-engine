from settlers_of_valgard.building.prototype.harvester import Harvester
from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.resource.resource import Meat
from settlers_of_valgard.settler.skill import Skill
from settlers_of_valgard.colors import Colors

Hunting = Skill("Hunting", Colors.GRASS)

hunters_hut = Harvester('Hunter\'s_Hut', Colors.GRASS, Hunting, [
    Bundle(), #1
    Bundle({Meat : 1}), #2
    Bundle({Meat : 2}), #3
    Bundle({Meat : 2}), #4
    Bundle({Meat : 2}), #5
    Bundle({Meat : 3}), #6
    Bundle({Meat : 3}), #7,
    Bundle({Meat : 4}), #8
])