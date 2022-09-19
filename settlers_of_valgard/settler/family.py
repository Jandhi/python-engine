from objects.game_object import GameObject
from objects.node import Node
from settlers_of_valgard.settler.settler import CreatedSettlerEvent, Settler

class FamilyMember(Node):
    def __init__(self, family) -> None:
        super().__init__()
        self._family : Family = family

    @property
    def family(self):
        return self._family

    @property.setter
    def family(self, value):
        if self._family is not None:
            self._family.members.remove(self)
        
        self._family : Family = value
        self._family.members.append(self)


class Family(Node):
    def __init__(self, members = None) -> None:
        super().__init__()

        self.residence = None
        self.members : list = members or []

def add_family_node(ev : CreatedSettlerEvent):
    ev.settler.add_child(FamilyMember(None))

CreatedSettlerEvent.add_listener(add_family_node)