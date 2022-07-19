from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype
from settlers_of_valgard.events.event import BlockableEvent
from settlers_of_valgard.processes.work import WorkEvent

class Workplace(BuildingPrototype):
    def __init__(self, name, color, workers = None) -> None:
        super().__init__(name, color)

        self.workers = workers or []

        for worker in self.workers:
            worker.workplace = self
    
    def add_worker(self, worker):
        if worker.workplace is not None:
            worker.workplace.remove_worker(worker)

        worker.workplace = self
        self.workers.append(worker)
    
    def remove_worker(self, worker):
        if worker in self.workers:
            worker.workplace = None
            self.workers.remove(worker)

    def work(self, worker, settlement):
        if WorkEvent(worker, self, settlement).send_is_success():
            self.__work(worker, settlement)
    
    def __work(self, worker, settlement):
        pass

