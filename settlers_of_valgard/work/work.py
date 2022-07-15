from settlers_of_valgard.events.event import BlockableEvent
from settlers_of_valgard.settlement import Settlement

def work(settlement : Settlement):
    for settler in settlement.settlers:
        if settler.workplace is not None:
            pass

def work_phase(settlement):
    for settler in settlement.settlers:
        work(settler, settlement)

def work(settler, settlement):
    if settler.workplace is not None:
        settler.workplace.work(settler, settlement)

class WorkEvent(BlockableEvent):
    def __init__(self, worker, workplace, settlement) -> None:
        super().__init__()
        self.worker = worker
        self.workplace = workplace
        self.settlement = settlement