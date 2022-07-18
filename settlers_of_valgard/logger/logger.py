from objects.game_object import find_object
from objects.static_object import StaticSingleton
from settlers_of_valgard.processes.day import DayEndEvent

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

def day_increaser(day_end : DayEndEvent):
    find_object(Logger).day = day_end.new_day

DayEndEvent.add_listener(day_increaser)