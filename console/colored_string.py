from colored import fg, attr
from console.colored_object import ColoredObject

class ColoredString:
    def __init__(self, contents, color) -> None:
        self.contents = contents
        self.color = color

    def __repr__(self) -> str:
        s = f'{fg(self.color)}'
    
        for part in self.contents:
            if isinstance(part, ColoredObject) or isinstance(part, ColoredObject):
                s = f'{s}{attr(0)}{part}{fg(self.color)}'
            elif isinstance(part, str):
                s = f'{s}{part}'

        return f'{s}{attr(0)}'
    
def color(str, color) -> ColoredString:
    c = ColoredString((str), color)
    return c 