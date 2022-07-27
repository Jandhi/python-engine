from objects.game_object import find_object
from settlers_of_valgard.events.event import BlockableEvent
from settlers_of_valgard.logger.logger import log
from settlers_of_valgard.logger.logging_level import Detailed, Everything
from settlers_of_valgard.processes.day import DaytimeStartEvent
from settlers_of_valgard.settlement import Settlement

def work(settlement : Settlement):
    for settler in settlement.settlers:
        if settler.workplace is not None:
            pass

def work(settler, settlement):
    if settler.workplace is not None:
        settler.workplace.work(settler, settlement)
        log(f'{settler} worked at {settler.workplace}', {Everything})
    else:
        log(f'{settler} does not have a workplace!', Detailed)

class WorkEvent(BlockableEvent):
    def __init__(self, worker, workplace, settlement) -> None:
        super().__init__()
        self.worker = worker
        self.workplace = workplace
        self.settlement = settlement

def tick_work(ev : DaytimeStartEvent):
    settlement = find_object(Settlement)
    for settler in settlement.settlers:
        work(settler, settlement)

DaytimeStartEvent.add_listener(tick_work)