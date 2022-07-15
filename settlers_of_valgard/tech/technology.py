from objects.static_object import StaticObject

class Technology(StaticObject):
    def __init__(self, name, color, required_tech = None) -> None:
        super().__init__(id = name)
        self.name = name
        self.color = color
        self.required_tech = required_tech or []