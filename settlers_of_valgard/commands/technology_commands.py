from console.command.command import Command
from console.command.tag import Tag
from objects.query import Query
from settlers_of_valgard.tech.technology import Technology

discovered_tag = Tag('-discovered', 'lists only discovered technologies', aliases=['-d', '-disc'])
def tech_execute(cmd):
    query = Query(Technology)

    # TODO 

tech_command = Command(
    'tech', 
    'displays information about technologies', 
    tech_execute, 
    aliases=['tc', 'technologies', 'technology', 'techno'],
    tags=[discovered_tag]
)