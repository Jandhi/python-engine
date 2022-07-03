from console.colored_string import color
from console.console import cprint
from console.palette import Palette

def cerror(error):
    print(f'{color("ERROR:", Palette.ERROR_COLOR)} {error}')