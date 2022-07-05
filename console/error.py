from console.colored_string import color
from console.console import cprint
from console.palette import Palette

def print_error(error):
    print(f'{color("ERROR:", Palette.ERROR_COLOR)} {error}')