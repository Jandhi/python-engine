from map.ticked import Ticked
from objects.enums.enum import OrderedEnum

from settlers_of_valgard.colors import Colors

class SpoilLevel(OrderedEnum):
    def __init__(self, name, color, value) -> None:
        super().__init__(name, color, value)

Spoiled = SpoilLevel('Spoiled', Colors.SWAMP, 0)
Old = SpoilLevel('Old', Colors.PINE, 1)
Fresh = SpoilLevel('Fresh', Colors.GRASS, 2)

class Spoilable(Ticked):
    def __init__(self, days_until_spoiled, age = 0) -> None:
        super().__init__()
        self.days_until_spoiled = days_until_spoiled
        self.age = age

    def on_tick(self, ticknum):
        self.age += 1
        
    def spoilage_level(self) -> SpoilLevel:
        if self.age >= self.days_until_spoiled:
            return Spoiled
        elif self.age >= self.days_until_spoiled / 2:
            return Old
        else:
            return Fresh
    
    def copy_self(self):
        return Spoilable(self.days_until_spoiled, self.age)