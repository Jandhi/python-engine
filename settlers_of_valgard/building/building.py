from objects.game_object import GameObject
from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype

class Building(GameObject):
    def __init__(self, prototype : BuildingPrototype) -> None:
        super().__init__()

        self.prototype = prototype
    
    def __get_name(self):
        return self.prototype.__get_name()
    
    def __get_color(self):
        return self.prototype.__get_color()
        
def make_building(prototype):
    return Building(prototype)

setattr(BuildingPrototype, 'make_building', make_building)