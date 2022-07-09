from typing import Pattern
from console.colored_string import color
from console.command.argument import Argument
from console.palette import Palette
from console.command.tag import Tag
from console.command.command import Command
from objects.query import CONTAINS, ENDS_WITH, STARTS_WITH, Query

class QueryCommand(Command):
    def __init__(self, name, description, type, 
        single_formatter = None, 
        list_formatter = None, 
        aliases=None, 
        arguments=None, 
        optional_arguments=None, 
        tags=None
    ) -> None:
        prefix_arg = Argument('prefix', f"the beginning of the {type}'s name")
        suffix_arg = Argument('suffix', f"the ending of the {type}'s name")
        suffix_tag = Tag('-suffix', '', ['-ends-with', '-ends', '-endswith', '-suf', '-sfx', '-suff'], [suffix_arg])
        midfix_arg = Argument('midfix', f"a string found in the middle of the {type}'s name")
        midfix_tag = Tag('-midfix', '', ['-mid', '-contains', '-containing'], [midfix_arg])

        def query(cmd):
            q = Query(type)

            if prefix_arg.value is not None:
                q = q.with_field('name', prefix_arg.value, STARTS_WITH)
            
            if suffix_arg.value is not None:
                q = q.with_field('name', suffix_arg.value, ENDS_WITH)
            
            if midfix_arg.value is not None:
                q = q.with_field('name', midfix_arg.value, CONTAINS)

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
                    if list_formatter is not None:
                        print(list_formatter(obj))
                    else:
                        print(obj)
            
        
        super().__init__(name, description, query, aliases, arguments, optional_arguments, tags)

        for tag in [
            suffix_tag, midfix_tag
        ]:
            self.tags.append(tag)

        for arg in [
            prefix_arg
        ]:
            self.optional_arguments.append(arg)