import asyncio
from faulthandler import is_enabled
from threading import Thread, Lock
from time import sleep

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
from objects.query import Query
from map.ticked import Ticked, tick

from textual.app import App
import textual.events as events


s = Settlement()
PlayerInfo()
Logger()

s.stockpile.add(Meat, 2)

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
        self.map_widget = map_widget
        await self.view.dock(self.map_widget)

        self.lock = Lock()
        self.started = False

        def loop():
            while True:
                tick()
                sleep(0.2)
            
        self.thread = Thread(target=loop)

        self.set_interval(0.05, self.map_widget.refresh)
    
    def on_key(self, event : events.Key):
        if not self.started:
            self.thread.start()    
            self.started = True

        if not self.map_widget.has_focus:
            return

        px, py = self.map_widget.pointer

        if event.key == 'up':
            self.map_widget.pointer = (px, max(py - 1, 0))
        if event.key == 'down':
            self.map_widget.pointer = (px, min(py + 1, self.map_widget.map.height - 1))
        if event.key == 'left':
            self.map_widget.pointer = (max(px - 1, 0), py)
        if event.key == 'right':
            self.map_widget.pointer = (min(px + 1, self.map_widget.map.width - 1), py)

        self.lock.acquire()
        self.map_widget.refresh()
        self.lock.release()
    
SettlersOfValgardApp.run()