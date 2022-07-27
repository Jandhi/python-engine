from objects.game_object import find_object
from objects.query import Query
from objects.static_object import StaticSingleton
from console.colored_string import ColoredString, color
from settlers_of_valgard.colors import Colors
from settlers_of_valgard.player_info import PlayerInfo
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

def log_warning(message, priority):
    Logger.instance.log(f'{color("[WARNING]", Colors.SUNSHINE)} {message}', priority)

def logger_day_end(day_end : DayEndEvent):
    logger : Logger = find_object(Logger)
    level = find_object(PlayerInfo).logging_level

    for msg, lvl in logger.contents[logger.day]:
        if lvl <= level:
            print(msg)
    
    logger.day = day_end.new_day

DayEndEvent.add_listener(logger_day_end)