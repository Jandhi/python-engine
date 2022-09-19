from objects.game_object import GameObject
from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype

class Building(GameObject):
    def __init__(self, prototype : BuildingPrototype) -> None:
        super().__init__()

        self.prototype = prototype
    
    def get_title(self):
        return self.prototype.get_title()
    
    def get_color(self):
        return self.prototype.get_color()
        
def make_building(prototype):
    return Building(prototype)

setattr(BuildingPrototype, 'make_building', make_building)