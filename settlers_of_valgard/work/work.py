from settlers_of_valgard.events.event import BlockableEvent

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