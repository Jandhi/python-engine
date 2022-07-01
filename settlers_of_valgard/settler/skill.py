from objects.static_object import StaticObject
from settlers_of_valgard.colors import GREEN


class Skill(StaticObject):
    def __init__(self, name, color) -> None:
        super().__init__(id=name)
        self.name = name
        self.color = color

Hunting = Skill("Hunting", GREEN)
