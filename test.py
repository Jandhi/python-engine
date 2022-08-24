from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from settlers_of_valgard.settler.settler import Settler

settler = Settler('test')

class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel(str(settler), style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class HoverApp(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        hovers = (Hover() for _ in range(10))
        await self.view.dock(*hovers, edge="left")


HoverApp.run(log="textual.log")