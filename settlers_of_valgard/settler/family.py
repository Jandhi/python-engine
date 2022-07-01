from objects.game_object import GameObject

class Family(GameObject):
    def __init__(self, settlers = None) -> None:
        super().__init__()

        self.settlers : list = settlers or []
        self.residence = None

        for settler in self.settlers:
            settler.family = self
    
    def add_settler(self, settler):
        if settler.family is not None:
            settler.family.remove_settler(settler)

        settler.family = self
        self.settlers.append(settler)
    
    def remove_settler(self, settler):
        if settler in self.settlers:
            settler.family = None
            self.settlers.remove(settler)