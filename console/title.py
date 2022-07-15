from console.colored_object import ColoredObject
from console.colored_string import ColoredString, color
from console.palette import Palette

def title(cstr : ColoredString):
    if isinstance(cstr, ColoredObject):
        cstr = color(cstr)

    s = f'{cstr.transform(lambda str : str.upper())}'
    bar = ''

    for i in range(len(cstr)):
        bar = f'{bar}-'
    
    return f'{color(bar, Palette.UNDERLINE)}\n{s}\n{color(bar, Palette.UNDERLINE)}'