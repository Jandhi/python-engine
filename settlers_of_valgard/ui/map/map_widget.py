from asyncio import events
from ctypes import pointer
from sqlite3 import connect
from rich.panel import Panel
from textual.widget import Widget
from textual.reactive import Reactive
import textual.events as events

from settlers_of_valgard.map.map import Map

class MapWidget(Widget, can_focus=True):
    has_focus: Reactive[bool] = Reactive(False)

    def __init__(self, map : Map, name: str | None = None) -> None:
        super().__init__(name)
        self.map = map
        self.pointer = (self.map.width // 2, self.map.height // 2)

    def render(self) -> Panel:
        content = ''
        px, py = self.pointer

        for y in range(self.size.height):
            for x in range(self.size.width - 4):
                map_x = x + px - self.size.width // 2
                map_y = y + py - self.size.height // 2

                if map_x == px and map_y == py:
                    content = f'{content}[red]X[/red]'
                elif 0 <= map_x < self.map.width and 0 <= map_y < self.map.height:
                    content = f'{content}{self.map.tiles[map_x][map_y]}'
                else:
                    content = f'{content} '

            content = f'{content}\n'

        return Panel(content)
    
    async def on_focus(self, event: events.Focus) -> None:
        self.has_focus = True

    async def on_blur(self, event: events.Blur) -> None:
        self.has_focus = False
