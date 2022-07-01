from objects.static_object import StaticObject
from settlers_of_valgard.colors import Colors


class Rank(StaticObject):
    def __init__(self, name, color) -> None:
        super().__init__(id=name)
        self.name = name
        self.color = color

FREEMAN = Rank('Freeman', Colors.GRASS)
HUSKARL = Rank('Huskarl', Colors.LAKE)
GOTHI   = Rank('Gothi',   Colors.FUR)
HIRDMAN = Rank('Hirdman', Colors.CRIMSON)
JARL    = Rank('Jarl',    Colors.MAGENTA)
KONUNG  = Rank('Konung',  Colors.GOLD)