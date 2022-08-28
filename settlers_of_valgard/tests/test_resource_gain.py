from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.resource.resource import Wood, send_to_stockpile, ResourceGainEvent
from settlers_of_valgard.settlement import Settlement
from events.game_event import add_listener

s = Settlement()

def modify(ev : ResourceGainEvent):
    ev.bundle *= 2

add_listener(ResourceGainEvent, modify)

b = Bundle(Wood.create(3))
send_to_stockpile(b)

assert(s.stockpile.count(lambda res : res.resource == Wood) == 6)