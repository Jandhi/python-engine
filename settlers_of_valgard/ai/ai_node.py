from map.ticked import Ticked

class AI(Ticked):
    def __init__(self) -> None:
        super().__init__()
        self.cooldown = 0
    
    def on_tick(self, ticknum):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.on_act(ticknum)
    
    def on_act(self, ticknum):
        pass

