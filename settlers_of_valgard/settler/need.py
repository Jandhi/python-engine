
from objects.enums.enum import NamedEnum

class Need(NamedEnum):
    def __init__(self, name, color) -> None:
        super().__init__(name, color)