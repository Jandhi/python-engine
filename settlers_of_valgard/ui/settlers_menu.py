from objects.query import Query
from objects.static_object import StaticObject
from settlers_of_valgard.menu import Menu, MenuAction
from settlers_of_valgard.ui.multi_page_menu import MultiPageMenu
from settlers_of_valgard.settler.settler import Settler
from settlers_of_valgard.ui.settlement_menu import settlement_menu

def get_settlers():
    return Query(Settler).all()

settlers_menu = MultiPageMenu('settlers menu', get_settlers, None)

go_to_settlers = MenuAction('settlers', settlers_menu.load, settlement_menu, key='s')
go_back_to_settlement = MenuAction('back', settlement_menu.load, settlers_menu, key='escape')

class SettlerMenu(Menu):
    def __init__(self) -> None:
        super().__init__('settler menu')
        self.settler : Settler = None
        self.renderers = []
    
    def set_settler(self, settler):
        self.settler = settler
    
    def get_title(self):
        return self.settler
    
    def get_text(self):
        s = ''

        for renderer in self.renderers:
            s = f'{s}{renderer(self.settler)}\n'
        
        return s

settler_menu = SettlerMenu()
go_back_to_settlers = MenuAction('back', settlers_menu.load, settler_menu, key='escape')
