from console.colored_string import ColoredString
from colored import fg, attr

def cprint(*args, color='white'):
    print(ColoredString(args, color))