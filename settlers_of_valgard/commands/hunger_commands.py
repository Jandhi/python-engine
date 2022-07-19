from console.command.query_command import QueryCommand
from console.command.tag import Tag
from settlers_of_valgard.processes.hunger import Hunger, get_hunger_status
from settlers_of_valgard.settler.settler import Settler

summary_tag = Tag('-summary', 'summarizes the hunger levels of settlers', aliases=['-sum', '-sm'])

def display_hunger(settler : Settler):
    return f'{settler} is {get_hunger_status(settler)}'

def list_hunger(settlers):
    s = ''

    if summary_tag.used:
        statuses = {}

        for settler in settlers:
            status = get_hunger_status(settler)
            
            if status in statuses:
                statuses[status] += 1
            else:
                statuses[status] = 1
        
        for status, count in sorted(statuses.items(), lambda pair : pair[0].value * -1):
            s = f'{s}{status}: {count}\n'
    else:
        for settler in settlers:
            s = f'{s}{settler}: {get_hunger_status(settler)}\n'
    
    return s

HungerCommand = QueryCommand(
    'hunger',
    'lists the hunger of settlers',
    Settler,
    single_formatter=display_hunger,
    whole_list_formatter=list_hunger
)