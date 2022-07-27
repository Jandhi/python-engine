from console.colored_string import ColoredString
from objects.game_object import find_object
from objects.query import Query
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.logger.logger import log, log_warning
from settlers_of_valgard.logger.logging_level import Detailed, Everything, Limited, Normal
from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.resource.food import EDIBLE
from settlers_of_valgard.resource.resource import Resource
from settlers_of_valgard.settler.need import Need
from settlers_of_valgard.settler.settler import CreatedSettlerEvent, Settler
from settlers_of_valgard.processes.day import DaytimeEndEvent
from settlers_of_valgard.settlement import Settlement
from objects.enums.enum import OrderedEnum

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

def add_hunger_need(ev : CreatedSettlerEvent):
    if Hunger not in ev.settler.needs:
        ev.settler.needs[Hunger] = 0

# adds hunger tracking to game
CreatedSettlerEvent.add_listener(add_hunger_need)

def tick_hunger(ev : DaytimeEndEvent):
    settlement : Settlement = find_object(Settlement)

    available_food = Bundle()
    fed_count = 0

    for res, amt in settlement.stockpile.contents.items():
        if res.has_tag(EDIBLE):
            available_food.add(res, amt)

    for settler in settlement.settlers:
        fed = False
        settler.needs[Hunger] += 1

        while get_hunger_status(settler) <= Hungry:
            resource : Resource = available_food.first()

            if resource is not None:
                available_food.remove(resource, 1)
                settlement.stockpile.remove(resource, 1)
                settler.needs[Hunger] -= resource.tags[EDIBLE]
                log(f'{settler} ate {resource}', Everything)
                fed = True
            else:
                log_warning(ColoredString([settler, ' could not find food!']), Detailed)
                break
        
        if fed:
            fed_count += 1
    
    log(f'{fed_count} settlers were fed', Normal)
    
    not_fed = Query(Settler).filter(lambda s : get_hunger_status(s) <= Hungry).count()
    if not_fed > 0:
        log_warning(f'{not_fed} settlers are hungry', Limited)

DaytimeEndEvent.add_listener(tick_hunger)