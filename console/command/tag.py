from console.command.argument_container import ArgumentContainer


class Tag(ArgumentContainer):
    def __init__(self, name, description, aliases = None, arguments=None, optional_arguments=None) -> None:
        super().__init__(name, arguments, optional_arguments)
        self.description = description
        self.aliases = aliases
        self.used = False
    
    def clear(self):
        self.used = False
        super().clear()