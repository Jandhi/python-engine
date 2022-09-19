import asyncio
from faulthandler import is_enabled
from logging import PlaceHolder
from threading import Thread, Lock
from time import sleep
from settlers_of_valgard.ui.multi_page_menu import MultiPageMenu

from settlers_of_valgard.ui.action_widget import ActionWidget

from .map.map import Map

from settlers_of_valgard.map.map_entity import MapEntity
from settlers_of_valgard.ai.settler_ai import SettlerAI
from settlers_of_valgard.logger.logger import Logger
from settlers_of_valgard.player_info import PlayerInfo
from settlers_of_valgard.processes.day import pass_day
from settlers_of_valgard.resource.food import Meat
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.settler.settler import Settler
import settlers_of_valgard.commands.work_commands
import settlers_of_valgard.commands.settler_commands
from settlers_of_valgard.processes.hunting.hunting import Hunting
import settlers_of_valgard.commands.hunger_commands 
import settlers_of_valgard.commands.log_commands
from settlers_of_valgard.ui.map.map_widget import MapWidget
from settlers_of_valgard.menu import Menu, MenuAction

from settlers_of_valgard.ui.settlement_menu import settlement_menu
import settlers_of_valgard.ui.settlers_menu

from objects.query import Query
from map.ticked import Ticked, tick

from textual.app import App
import textual.events as events
from textual.widgets import ScrollView, Placeholder


s = Settlement()
PlayerInfo()
Logger()

s.stockpile.add(Meat.create(2))

s.settlers = [
    Settler('Bjorn'),
    Settler('Norn'),
    Settler('Vorn')
]

s.settlers[2].add_xp(Hunting, 100)

pass_day(0)

vorn = s.settlers[2]
vorn.add_child(SettlerAI())

map = Map(50, 50)
map_widget = MapWidget(map)

class SettlersOfValgardApp(App):
    async def on_mount(self) -> None:
        Menu.app = self
        self.map_widget = map_widget

        self.action_widget = ActionWidget()
        self.log_widget = ScrollView('test')

        #await self.view.dock(self.action_widget, edge="right")
        await self.view.dock(self.log_widget, self.action_widget, edge="right")

        self.refresh()
        self.action_widget.refresh()
        self.log_widget.refresh()

        settlement_menu.load()
    
    def on_key(self, event : events.Key):
        if self.action_widget.callbacks is not None and event.key in self.action_widget.callbacks:
            self.action_widget.callbacks[event.key]()
            self.action_widget.refresh()
            self.log_widget.refresh()
    
    def load(self, action_group : Menu):
        self.action_widget.action_group = action_group
        self.action_widget.refresh()
    
SettlersOfValgardApp.run()