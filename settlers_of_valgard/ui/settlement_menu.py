from settlers_of_valgard.menu import Menu, MenuAction
from settlers_of_valgard.ui.confirmation_menu import get_confirmation

from textual.events import ShutdownRequest

settlement_menu = Menu('settlement menu', 'Choose an action below:')

def quit():
    1 / 0

quit_out = MenuAction(
    'Quit', 
    lambda : get_confirmation('Are you sure you want to quit? Unsaved progress will be lost!', quit, settlement_menu.load), 
    settlement_menu, 
    'q'
)