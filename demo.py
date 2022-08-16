from random import randint
from asciimatics.screen import Screen
from settlers_of_valgard.settler.settler import Settler
from colored import fg

settler = Settler('test')

def demo(screen):
    while True:
        screen.print_at('test', 10, 10, colour=10)
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

Screen.wrapper(demo)