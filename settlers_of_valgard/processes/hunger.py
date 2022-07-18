from settlers_of_valgard.colors import Colors
from settlers_of_valgard.settler.need import Need
from settlers_of_valgard.settler.settler import CreatedSettlerEvent, Settler
from objects.enums.enum import NamedEnum
from console.command.query_command import QueryCommand

Hunger = Need('Hunger', Colors.FUR)

class HungerStatus(NamedEnum):
    def __init__(self, name, color) -> None:
        super().__init__(name, color)

Full = HungerStatus('Full', Colors.GRASS)
Hungry = HungerStatus('Hungry', Colors.SUNSHINE)
Famished = HungerStatus('Famished', Colors.ORANGE)
Starving = HungerStatus('Starving', Colors.RED)

def get_hunger_status(settler : Settler):
    if settler.needs[Hunger] < 1:
        return Full
    elif settler.needs[Hunger] < 2:
        return Hungry
    elif settler.needs[Hunger] < 3:
        return Famished
    else:
        return Starving

def add_hunger(settler : Settler):
    if Hunger not in settler.needs:
        settler.needs[Hunger] = 0

# adds hunger tracking to game
CreatedSettlerEvent.add_listener(add_hunger)

HungerCommand = QueryCommand(
    'hunger',
    'lists the hunger of settlers',
    Settler,
    # TODO
)