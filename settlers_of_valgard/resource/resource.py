from objects.game_object import GameObject, find_object
from objects.node import Node
from objects.static_object import StaticNode
from objects.util import compare_without_ids
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.events.event import BlockableEvent
from settlers_of_valgard.settlement import Settlement

class ResourceType(StaticNode):
    def __init__(self, name, color, children : list[Node] = None, on_create = None) -> None:
        super().__init__(name)
        self.name = name
        self.color = color
        self.children = children or []
        self.on_create = on_create

    def on_create(self, resource):
        pass

    def create(self, amt):
        res = Resource(self, amt)

        if self.on_create is not None:
            self.on_create(res)

        for child in self.children:
            res.add_child(child.copy())
        
        return res

    def __mul__(self, num : int):
        assert(isinstance(num, int))
        return self.create(num)
    
    def __rmul__(self, num : int):
        assert(isinstance(num, int))
        return self.create(num)

class Resource(Node):
    class Schema(Node.Schema):
        do_not_pool = True

    def __init__(self, resource : ResourceType, amount : int) -> None:
        super().__init__()
        self.resource = resource
        self.amount = amount
    
    def is_stackable(self, other: object) -> bool:
        if isinstance(other, Resource):
            return compare_without_ids(self, other)
        
        return super().__eq__(other)
    
    def copy_self(self):
        return Resource(self.type, self.amount)
    
    def with_amount(self, amt):
        self.amount = amt
        return self
    
    def split_off(self, amt):
        if amt > self.amount:
            return None

        cp : Resource = self.copy()
        cp.amount = amt
        self.amount -= amt
        return cp

Wood = ResourceType('Wood', Colors.WOOD)

def send_to_stockpile(bundle):
    if ResourceGainEvent(bundle).send_is_success():
        find_object(Settlement).stockpile += bundle

class ResourceGainEvent(BlockableEvent):
    def __init__(self, bundle) -> None:
        super().__init__()

        self.bundle = bundle