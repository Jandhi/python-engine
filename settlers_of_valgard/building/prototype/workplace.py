from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype

class Workplace(BuildingPrototype):
    def __init__(self, name, workers = None) -> None:
        super().__init__(name)

        self.workers = workers or []

        for worker in workers:
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