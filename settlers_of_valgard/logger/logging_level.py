from objects.enums.enum import OrderedEnum
from settlers_of_valgard.colors import Colors

class LogDetailLevel(OrderedEnum):
    def __init__(self, name, color, value) -> None:
        super().__init__(name, color, value)

Least = LogDetailLevel('Least', Colors.CRIMSON, 1) 
Limited = LogDetailLevel('Limited', Colors.SUNSHINE, 2)
Normal = LogDetailLevel('Normal', Colors.GRASS, 3)
Detailed = LogDetailLevel('Detailed', Colors.JADE, 4)
Everything = LogDetailLevel('Everything', Colors.MAGENTA, 5)