from console.colored_object import ColoredObject
from colored import fg, attr

def cprint(*args, color='white'):
    s = f'{fg(color)}'
    
    for arg in args:
        if isinstance(arg, ColoredObject):
            s = f'{s}{arg}{fg(color)}'
        elif isinstance(arg, str):
            s = f'{s}{arg}'

    s = f'{s}{attr(0)}'
    
    print(s)