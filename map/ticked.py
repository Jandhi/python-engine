from objects.node import Node

ticklist = []
ticknum = 0

class Ticked(Node):
    def __init__(self) -> None:
        super().__init__()
        self.add_to_ticklist()
    
    def post_construction(self) -> None:
        self.add_to_ticklist()
        return super().post_construction()
    
    def add_to_ticklist(self):
        ticklist.append(self)

    def on_tick(self, ticknum):
        pass
    
    def on_delete(self) -> None:
        ticklist.remove(self)

def tick():
    global ticknum
    global ticklist

    for ticked in ticklist:
        ticked : Ticked
        ticked.on_tick(ticknum)

    
    ticknum += 1