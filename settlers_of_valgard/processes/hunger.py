from heapq import heapify, heappop, heappush
import heapq
from console.colored_string import ColoredString
from objects.game_object import find_object
from objects.node import Node
from objects.query import Query
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.logger.logger import log, log_warning
from settlers_of_valgard.logger.logging_level import Detailed, Everything, Limited, Normal
from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.resource.food import EdibleNode
from settlers_of_valgard.resource.resource import Resource, ResourcePrototype
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

    for res in settlement.stockpile.contents:
        res : Resource
        if res.has_child(EdibleNode):
            available_food.add(res)

    hungry_nodes = Query(HungerNode).filter(lambda node : node.amount > 0).all()

    queue = heapify([(node.amount * -1, node) for node in hungry_nodes]) # smallest is hungriest

    while len(available_food.contents) > 0 and len(queue) > 0:
        hungriest : HungerNode = heappop(queue)
        first_food : Resource = available_food.contents.first()
        edible_node : EdibleNode = first_food.find_child(EdibleNode)

        hungriest.amount -= edible_node.satiation
        available_food.remove(first_food, 1)
        settlement.stockpile.remove(first_food, 1)
        fed_count += 1

        if hungriest.amount > 0:
            heappush(queue, hungriest)
    
    log(f'{fed_count} settlers were fed', Normal)
    
    hungry_count = Query(HungerNode).filter(lambda n : n.status() <= Hungry).count()
    if hungry_count > 0:
        log_warning(f'{hungry_count} settlers are still hungry', Limited)

DaytimeEndEvent.add_listener(tick_hunger)