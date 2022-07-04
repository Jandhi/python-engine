from typing import Pattern
from console.colored_string import color
from console.command.argument import Argument
from console.palette import Palette
from console.command.tag import Tag
from console.command.command import Command
from objects.query import STARTS_WITH, Query

class QueryCommand(Command):
    def __init__(self, name, description, type, 
        single_formatter = None, 
        in_list_formatter = None, 
        aliases=None, 
        arguments=None, 
        optional_arguments=None, 
        tags=None
    ) -> None:
        prefix_arg = Argument("prefix", f"the prefix of the {type}")
        
        def query(cmd):
            q = Query(type)

            if prefix_arg.value is not None:
                q = q.with_field('name', prefix_arg.value, STARTS_WITH)

            objs = q.all()
            if len(objs) == 0:
                print(color("None found!", Palette.ERROR_COLOR))
            elif len(objs) == 1:
                if single_formatter is not None:
                    print(single_formatter(objs[0]))
                else:
                    print(objs[0])
            else:
                for obj in objs:
                    if in_list_formatter is not None:
                        print(in_list_formatter(obj))
                    else:
                        print(obj)
            
        
        super().__init__(name, description, query, aliases, arguments, optional_arguments, tags)

        for tag in [
            
        ]:
            self.tags.append(tag)

        for arg in [
            prefix_arg
        ]:
            self.optional_arguments.append(arg)