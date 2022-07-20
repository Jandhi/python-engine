from console.command.command import Command
from console.command.scopes import IN_GAME
from console.command.tag import Tag
from console.title import title
from objects.game_object import find_object
from objects.query import Query
from settlers_of_valgard.settlement import Settlement
from settlers_of_valgard.tech.technology import DISCOVERED, LOCKED, Technology

status_tag = Tag('-status', 'lists only discovered technologies of certain status', aliases=['-s', '-stat'])
def tech_execute(cmd):
    query = Query(Technology)

    settlement : Settlement = find_object(Settlement)
    title_text = 'Unlocked Technologies'
    
    print(title(title_text))

    #TODO
    
    for tech in query.all():
        print(tech)


tech_command = Command(
    'tech', 
    'displays information about technologies', 
    tech_execute, 
    aliases=['tc', 'technologies', 'technology', 'techno'],
    tags=[status_tag],
    scope=IN_GAME
)