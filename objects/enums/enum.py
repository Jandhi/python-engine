from objects.query import Query
from objects.static_object import StaticObject

class NamedEnum(StaticObject):
    type = '__named_enum'

    def __init__(self, name, color) -> None:
        super().__init__(id=name)
        self.name = name
        self.color = color

class OrderedEnum(NamedEnum):
    type = '__ordered_enum'

    def __init__(self, name, color, value) -> None:
        super().__init__(name, color)

        self.value = value
    
    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __ne__(self, other) -> bool:
        return self.value != other.value
    
    def __lt__(self, other) -> bool:
        return self.value < other.value
    
    def __le__(self, other) -> bool:
        return self.value <= other.value
    
    def __gt__(self, other) -> bool:
        return self.value > other.value
    
    def __ge__(self, other) -> bool:
        return self.value >= other.value

def getEnum(value, type):
    return Query(type).filter(lambda obj : obj.value == value).first()