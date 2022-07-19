from ast import alias
from console.colored_string import ColoredString, color
from console.command.query_command import QueryCommand
from console.title import title
from settlers_of_valgard.settler.settler import Settler
from settlers_of_valgard.colors import Colors

def settler_formatter(settler : Settler):
    s = f'{title(settler)}\n'
    
    return s

settler_cmd = QueryCommand(
    "settlers", 
    "lists the settlers of your settlement",
    Settler,
    aliases=["s", "settler"],
    single_formatter=settler_formatter
)

def skills_formatter(settler : Settler):
    if len(settler.xp.keys()) > 0:
        cs = ColoredString((settler, " skills"))
        s = f'{title(cs)}\n'

        for skill in settler.xp:
            s = f'{s}{skill} - {settler.get_skill_level(skill)}'
    else:
        s = f'{settler} has no skills'

    return s

skill_cmd = QueryCommand(
    "skills",
    "lists the skills of a settler",
    Settler,
    aliases=["skill", "skl", "sk"],
    single_formatter=skills_formatter,
)