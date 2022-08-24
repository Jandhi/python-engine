from colored import fg, attr, colored

name_table = {int(num) : name for name, num in colored(0).paint.items()}

class ColoredObject:
    color = None
    name = None

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color
    
    def get_name(self):
        if self.name is None:
            return type(self).__name__
        
        return self.name
    
    def __str__(self) -> str:
        cname = name_table[self.get_color()]
        return f'[{cname}]{self.get_name()}[/{cname}]'
        
        return f'{fg(self.get_color()) if self.color else ""}{self.get_name()}{attr(0)}'