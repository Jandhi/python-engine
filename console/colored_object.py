from colored import fg, attr

class ColoredObject:
    color = None
    name = None

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __get_color(self):
        return self.color
    
    def __get_name(self):
        if self.name is None:
            return type(self).__name__
        
        return self.name
    
    def __str__(self) -> str:
        return f'{fg(self.__get_color()) if self.color else ""}{self.__get_name()}{attr(0)}'