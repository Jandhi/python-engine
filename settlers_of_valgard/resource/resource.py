from objects.game_object import GameObject, find_object
from objects.static_object import StaticObject
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.events.event import BlockableEvent
from settlers_of_valgard.settlement import Settlement

class Resource(StaticObject):
    def __init__(self, name, color, tags = None) -> None:
        super().__init__(name)
        self.name = name
        self.color = color
        self.tags : dict[str,] = tags or {}

    def has_tag(self, tag):
        return tag in self.tags

Wood = Resource('Wood', Colors.WOOD)

def send_to_stockpile(bundle):
    if ResourceGainEvent(bundle).send_is_success():
        find_object(Settlement).stockpile += bundle

class ResourceGainEvent(BlockableEvent):
    def __init__(self, bundle) -> None:
        super().__init__()

        self.bundle = bundle