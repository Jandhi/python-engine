from objects.static_object import StaticObject
from settlers_of_valgard.rank import Freeman

class Technology(StaticObject):
    def __init__(self, name, color, required_tech = None, required_rank = Freeman) -> None:
        super().__init__(id = name)
        self.name = name
        self.color = color
        self.required_tech = required_tech or []
        self.required_rank = required_rank