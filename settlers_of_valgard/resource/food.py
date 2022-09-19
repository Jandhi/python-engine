from objects.node import Node
from settlers_of_valgard.resource.resource import ResourcePrototype
from settlers_of_valgard.colors import Colors

class EdibleNode(Node):
    def __init__(self, satiation=1) -> None:
        super().__init__()
        self.satiation = satiation

    def copy_self(self):
        return EdibleNode(self.satiation)

Meat = ResourcePrototype(
    'Meat', 
    Colors.SALMON,
    [EdibleNode(2)],
)

