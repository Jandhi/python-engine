from objects.game_object import find_object
from objects.query import Query
from objects.singleton import Singleton
from settlers_of_valgard.logger.logger import Logger
from settlers_of_valgard.processes.day import DayEndEvent
from settlers_of_valgard.resource.bundle import Bundle

class Settlement(Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.day = 0
        self.settlers = []
        self.buildings = []
        self.stockpile = Bundle()
        self.unlocked_blueprints = []
        self.discovered_technologies = []

def day_increaser(day_end : DayEndEvent):
    find_object(Settlement).day = day_end.new_day

DayEndEvent.add_listener(day_increaser)