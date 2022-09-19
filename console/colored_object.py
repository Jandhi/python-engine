from colored import fg, attr, colored

name_table = {int(num) : name for name, num in colored(0).paint.items()}

class ColoredObject:
    color = None
    text = None

    def __init__(self, name, color):
        self.text = name
        self.color = color

    def get_color(self):
        return self.color
    
    def get_title(self):
        if hasattr(self, 'get_name'):
            return self.get_name()

        if hasattr(self, 'name'):
            return self.name

        if self.text is None:
            return type(self).__name__
        
        return self.text
    
    def __str__(self) -> str:
        color = self.get_color()
        cname = name_table[color] if isinstance(color, int) else color
        return f'[{cname}]{self.get_title()}[/{cname}]'
        
        #return f'{fg(self.get_color()) if self.color else ""}{self.get_name()}{attr(0)}'