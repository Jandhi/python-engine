from os import system
from typing import Callable
from console.console import cprint
from objects.query import Query
from objects.static_object import StaticObject

from textual.app import App

class MenuAction(StaticObject):
    class Schema(StaticObject.Schema):
        numeric_id = True

    def __init__(self, text, callback, menu : str | None = None, key=None, is_available=True) -> None:
        super().__init__(None)

        if isinstance(menu, Menu):
            menu = menu.name

        self.text : str = text
        self.callback : Callable = callback
        self.menu : str | None = menu
        self.key : str | None = key
        self.is_available : bool = is_available

class Menu(StaticObject):
    app : App = None

    def __init__(self, name, text = None, underline_color = "gray", footer : str | None = None) -> None:
        super().__init__(id=name)
        self.name = name
        self.text = text
        self.underline_color = underline_color
        self.footer = footer

    def get_title(self):
        return self.name
    
    def get_text(self):
        return self.text

    def get_footer(self):
        return self.footer
    
    def fetch_actions(self) -> list[MenuAction]:
        return Query(MenuAction).with_field('group', self.name).all()
    
    def build_actions(self) -> list[MenuAction]:
        return []

    def get_actions(self) -> list[MenuAction]:
        return self.build_actions() + self.fetch_actions()
    
    def load(self):
        Menu.app.load(self)