from objects.game_object import GameObject
from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype
from settlers_of_valgard.resource.bundle import Bundle

class Blueprint(GameObject):
    def __init__(self, building : BuildingPrototype, cost : Bundle) -> None:
        super().__init__()

        self.building = building
        self.cost = cost