from events.game_event import GameEvent
from objects.enums.enum import OrderedEnum
from objects.static_object import StaticObject
from settlers_of_valgard.colors import Colors


class Rank(OrderedEnum):
    def __init__(self, name, color, value) -> None:
        super().__init__(name, color, value)

Freeman = Rank('Freeman', Colors.GRASS,     0)
Huskarl = Rank('Huskarl', Colors.LAKE,      1)
Gothi   = Rank('Gothi',   Colors.FUR,       2)
Hirdman = Rank('Hirdman', Colors.CRIMSON,   3)
Jarl    = Rank('Jarl',    Colors.MAGENTA,   4)
Konung  = Rank('Konung',  Colors.GOLD,      5)

RANKS = [Freeman, Huskarl, Gothi, Hirdman, Jarl, Konung]

class RankChangeEvent(GameEvent):
    def __init__(self, old_rank, new_rank) -> None:
        super().__init__()
        self.old_rank = old_rank
        self.new_rank = new_rank