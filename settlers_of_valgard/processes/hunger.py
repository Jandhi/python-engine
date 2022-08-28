from console.colored_string import ColoredString
from objects.game_object import find_object
from objects.node import Node
from objects.query import Query
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.logger.logger import log, log_warning
from settlers_of_valgard.logger.logging_level import Detailed, Everything, Limited, Normal
from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.resource.food import EDIBLE
from settlers_of_valgard.resource.resource import ResourceType
from settlers_of_valgard.settler.settler import CreatedSettlerEvent, Settler
from settlers_of_valgard.processes.day import DaytimeEndEvent
from settlers_of_valgard.settlement import Settlement
from objects.enums.enum import OrderedEnum

class HungerStatus(OrderedEnum):
    def __init__(self, name, color, value) -> None:
        super().__init__(name, color, value)

Full = HungerStatus('Full', Colors.GRASS, 3)
Hungry = HungerStatus('Hungry', Colors.SUNSHINE, 2)
Famished = HungerStatus('Famished', Colors.ORANGE, 1)
Starving = HungerStatus('Starving', Colors.RED, 0)

class HungerNode(Node):
    def __init__(self) -> None:
        super().__init__()
        self.amount = 0

    def status(self):
        if self.amount < 1:
            return Full
        elif self.amount < 2:
            return Hungry
        elif self.amount < 3:
            return Famished
        else:
            return Starving

def add_hunger_need(ev : CreatedSettlerEvent):
    ev.settler.add_child(HungerNode())

# adds hunger tracking to game
CreatedSettlerEvent.add_listener(add_hunger_need)

def tick_hunger(ev : DaytimeEndEvent):
    settlement : Settlement = find_object(Settlement)

    available_food = Bundle()
    fed_count = 0

    for res, amt in settlement.stockpile.contents.items():
        if res.has_tag(EDIBLE):
            available_food.add(res, amt)

    for node in Query(HungerNode).all():
        node : HungerNode
        fed = False
        node.amount += 1

        while node.status() <= Hungry:
            resource : ResourceType = available_food.first()

            if resource is not None:
                available_food.remove(resource, 1)
                settlement.stockpile.remove(resource, 1)
                node.amount -= resource.tags[EDIBLE]
                log(f'{node.parent} consumed {resource}', Everything)
                fed = True
            else:
                log_warning(ColoredString([node.parent, ' could not find food!']), Detailed)
                break
        
        if fed:
            fed_count += 1
    
    log(f'{fed_count} settlers were fed', Normal)
    
    not_fed = Query(HungerNode).filter(lambda n : n.status() <= Hungry).count()
    if not_fed > 0:
        log_warning(f'{not_fed} settlers are hungry', Limited)

DaytimeEndEvent.add_listener(tick_hunger)