from objects.game_object import delete_game_object, find_object
from objects.query import Query
from settlers_of_valgard.menu import Menu, MenuAction

confirmation = 'confirmation'

def get_confirmation(question, on_yes, on_no):
    for action in Query(MenuAction).with_field('group', confirmation).all():
        delete_game_object(action)
    
    gp = Menu(confirmation, question)

    yes = MenuAction('yes', on_yes, gp, 'y')
    no = MenuAction('no', on_no, gp, 'n')

    gp.load()