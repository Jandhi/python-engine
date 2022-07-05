from console.colored_string import color
from console.error import print_error
from console.palette import Palette

def get_verification(question) -> bool:
    while True:
        y = color('y', Palette.INPUT_COLOR)
        n = color('n', Palette.INPUT_COLOR)
        print(f'{question} ({y}/{n})')

        s = input()

        if s.lower() in ('y', 'yes', 'ye'):
            return True
        
        if s.lower() in ('n', 'no'):
            return False
        
        y = color('"y"', Palette.INPUT_COLOR)
        n = color('"n"', Palette.INPUT_COLOR)
        print_error(f'You must answer with {y} or {n}')
    