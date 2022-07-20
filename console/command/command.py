from console.command.argument_container import ArgumentContainer
from console.command.scopes import GLOBAL
from console.palette import Palette
from objects.static_object import StaticObject

class Command(StaticObject, ArgumentContainer):
    def __init__(self, name, description, execute, 
        aliases = None, 
        arguments = None, 
        optional_arguments = None,
        tags = None,
        scope = GLOBAL,
    ) -> None:
        StaticObject.__init__(self, id=name)
        ArgumentContainer.__init__(self, arguments, optional_arguments)
        self.name = name
        self.execute = execute
        self.description = description
        self.aliases = aliases or []
        self.tags = tags or []
        self.scope = scope
        self.color = Palette.GREEN
        self.called_as = None
    
    def fill(self, args):
        i = 0
        min = self.min_arguments()

        while len(args) > 0:
            arg = args.pop(0)
            tag = self.find_tag(arg)

            if tag is not None:
                tag.fill(args)
                tag.used = True
                continue

            if i < len(self.arguments):
                self.arguments[i].fill(arg)
            else:
                self.optional_arguments[i - min].fill(arg)
    
    def find_tag(self, name):
        for tag in self.tags:
            if tag.name == name or name in tag.aliases:
                return tag
    
    def clear(self):
        for tag in self.tags:
            tag.clear()
        
        self.called_as = None

        return super().clear()