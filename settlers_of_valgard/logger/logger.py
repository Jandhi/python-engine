from objects.game_object import find_object
from objects.static_object import StaticSingleton

class Logger(StaticSingleton):
    instance = None

    def __init__(self) -> None:
        super().__init__()
        self.contents = {}
        self.day = 0
        
        Logger.instance = self
    
    def log(self, message, priority):
        if self.day not in self.contents:
            self.contents[self.day] = []
        
        self.contents[self.day].append((message, priority))

def log(message, priority):
    Logger.instance.log(message, priority)