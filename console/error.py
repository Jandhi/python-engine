from console.colored_object import color
from console.console import cprint

ERROR_COLOR = 'red'

def cerror(*args):
    cprint(color("ERROR:", ERROR_COLOR), ' ', *args)