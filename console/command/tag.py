from console.command.argument_container import ArgumentContainer


class Tag(ArgumentContainer):
    def __init__(self, name, description, aliases = None, arguments=None, optional_arguments=None) -> None:
        super().__init__(arguments, optional_arguments)
        self.name = name
        self.description = description
        self.aliases = aliases