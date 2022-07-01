from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype

class Residence(BuildingPrototype):
    def __init__(self, name : str, color : str, capacity : int, families = None) -> None:
        super().__init__(name)

        self.capacity = capacity
        self.families : list = families or []
    
    def add_family(self, family):
        if family.residence is not None:
            family.residence.remove_family(family)

        family.residence = self
        self.families.append(family)
    
    def remove_family(self, family):
        if family in self.families:
            family.residence = None
            self.families.remove(family)