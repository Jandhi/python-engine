from objects.game_object import GameObject
from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype

class Blueprint(GameObject):
    def __init__(self, building : BuildingPrototype) -> None:
        super().__init__()

        self.building = building