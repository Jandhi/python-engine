

class Argument:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.value = None

    def fill(self, value):
        self.value = value

class IntegerArgument(Argument):
    def __init__(self, name, description) -> None:
        super().__init__(name, description)
    
    def verify(self, value):
        try:
            self.value = int(value)
        except ValueError:
            raise ValueError(f'Argument {self.name} expects an integer. Received "{value}".')