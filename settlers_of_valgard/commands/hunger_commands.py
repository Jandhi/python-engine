from console.command.query_command import QueryCommand
from console.command.scopes import IN_GAME
from console.command.tag import Tag
from settlers_of_valgard.processes.hunger import HungerNode
from settlers_of_valgard.settler.settler import Settler

summary_tag = Tag('-summary', 'summarizes the hunger levels of settlers', aliases=['-sum', '-sm'])

def display_hunger(node : HungerNode):
    return f'{node.parent} is {node.status()}'

def list_hunger(nodes : list[HungerNode]):
    s = ''

    if summary_tag.used:
        statuses = {}

        for node in nodes:
            status = node.status()
            
            if status in statuses:
                statuses[status] += 1
            else:
                statuses[status] = 1
        
        for status, count in sorted(statuses.items(), lambda pair : pair[0].value * -1):
            s = f'{s}{status}: {count}\n'

        s = s[:-1]
    else:
        for node in nodes:
            s = f'{s}{node.parent}: {node.status()}\n'
        
        s = s[:-1]
    
    return s

HungerCommand = QueryCommand(
    'hunger',
    'lists the hunger of settlers',
    HungerNode,
    single_formatter=display_hunger,
    whole_list_formatter=list_hunger,
    scope=IN_GAME
)