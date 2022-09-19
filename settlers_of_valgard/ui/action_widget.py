from typing import Callable
from textual.widget import Widget
from console.colored_string import color
from settlers_of_valgard.menu import Menu
from textual.widget import Panel

class ActionWidget(Widget):
    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
        self.action_group : Menu | None = None
        self.callbacks : dict[str, Callable] = None

    def render(self):
        group = self.action_group
        
        if group is None:
            return ''
        
        s = group.get_title()
        s = f'{s}\n[{group.underline_color}]{"-" * len(s)}[/{group.underline_color}]\n{group.get_text()}\n'

        counter = 0
        self.callbacks = {}

        for action in group.get_actions():
            key = action.key
            
            if action.key is None:
                counter += 1
                key = str(counter)

            s = f'{s}{key}: {action.text}\n'
            
            self.callbacks[key] = action.callback

        if group.get_footer() is not None:
            s = f'{s}{group.get_footer()}\n'
        
        return Panel(s)