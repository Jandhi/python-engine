from objects.game_object import find_object
from objects.node import Node
from objects.query import Query
from settlers_of_valgard.events.event import BlockableEvent
from settlers_of_valgard.logger.logger import log
from settlers_of_valgard.logger.logging_level import Detailed, Everything
from settlers_of_valgard.processes.day import DaytimeStartEvent
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.settler.settler import Settler, CreatedSettlerEvent

class WorkerNode(Node):
    def __init__(self, workplace) -> None:
        super().__init__()
        self.workplace = workplace

    def work(self):
        if self.workplace is None:
            log(f'{self.parent} does not have a workplace!', Detailed)
        elif WorkEvent(self.parent, self).send_is_success():
            log(f'{self.parent} worked at {self.workplace}', {Everything})

def add_worker_node(ev : CreatedSettlerEvent):
    ev.settler.add_child(WorkerNode(None))

CreatedSettlerEvent.add_listener(add_worker_node)

class WorkEvent(BlockableEvent):
    def __init__(self, worker, workplace) -> None:
        super().__init__()
        self.worker = worker
        self.workplace = workplace

def tick_work(ev : DaytimeStartEvent):
    for worker_node in Query(WorkerNode).all():
        worker_node : WorkerNode
        worker_node.work()

DaytimeStartEvent.add_listener(tick_work)