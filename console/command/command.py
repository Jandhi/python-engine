from console.command.argument_container import ArgumentContainer
from objects.static_object import StaticObject

class Command(StaticObject, ArgumentContainer):
    def __init__(self, name, description, execute, 
        aliases = None, 
        arguments = None, 
        optional_arguments = None,
        tags = None,
    ) -> None:
        StaticObject.__init__(self, id=name)
        ArgumentContainer.__init__(self, arguments, optional_arguments)
        self.name = name
        self.execute = execute
        self.description = description
        self.aliases = aliases or []
        self.tags = tags or []