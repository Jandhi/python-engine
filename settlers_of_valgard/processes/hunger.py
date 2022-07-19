from settlers_of_valgard.colors import Colors
from settlers_of_valgard.settler.need import Need
from settlers_of_valgard.settler.settler import CreatedSettlerEvent, Settler
from objects.enums.enum import OrderedEnum
from console.command.query_command import QueryCommand

Hunger = Need('Hunger', Colors.FUR)

class HungerStatus(OrderedEnum):
    def __init__(self, name, color, value) -> None:
        super().__init__(name, color, value)

Full = HungerStatus('Full', Colors.GRASS, 3)
Hungry = HungerStatus('Hungry', Colors.SUNSHINE, 2)
Famished = HungerStatus('Famished', Colors.ORANGE, 1)
Starving = HungerStatus('Starving', Colors.RED, 0)

def get_hunger_status(settler : Settler):
    if settler.needs[Hunger] < 1:
        return Full
    elif settler.needs[Hunger] < 2:
        return Hungry
    elif settler.needs[Hunger] < 3:
        return Famished
    else:
        return Starving

def add_hunger(ev : CreatedSettlerEvent):
    if Hunger not in ev.settler.needs:
        ev.settler.needs[Hunger] = 0

# adds hunger tracking to game
CreatedSettlerEvent.add_listener(add_hunger)