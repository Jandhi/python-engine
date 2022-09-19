from colored import fg, attr
from console.colored_object import ColoredObject

class ColoredString:
    def __init__(self, contents, color=None) -> None:
        self.contents = contents
        self.color = color

    def color_code(self):
        return fg(self.color) if self.color is not None else ''

    def __repr__(self) -> str:
        s = f'{self.color_code()}'
    
        for part in self.contents:
            if isinstance(part, ColoredObject) or isinstance(part, ColoredString):
                s = f'{s}{attr(0)}{part}{self.color_code()}'
            elif isinstance(part, str):
                s = f'{s}{part}'

        return f'{s}{attr(0)}'
    
    def __len__(self) -> int:
        length = 0

        for part in self.contents:
            if isinstance(part, ColoredObject):
                length += len(part.get_title())
            else:
                length += len(part)
        
        return length
    
    def normalize(self):
        contents = []


        for part in self.contents:
            if isinstance(part, ColoredObject):
                contents.append(ColoredString([part.get_title()], part.get_color()))
            else:
                contents.append(part)
        
        self.contents = contents
    
    def transform(self, func):
        self.normalize()
        contents = []

        for part in self.contents:
            if isinstance(part, ColoredString):
                contents.append(part.transform(func))
            else:
                contents.append(func(part))
        
        self.contents = contents

        return self
    
def color(str, color=None) -> ColoredString:
    c = ColoredString([str], color)
    return c 