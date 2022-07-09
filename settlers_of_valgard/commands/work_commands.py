from console.command.argument import Argument
from console.command.command import Command
from objects.game_object import find_object
from objects.query import Query
from console.error import print_error
from console.colored_string import color
from console.palette import Palette
from settlers_of_valgard.building.prototype.building_prototype import BuildingPrototype
from settlers_of_valgard.building.prototype.harvester import Harvester
from settlers_of_valgard.resource.bundle import Bundle
from settlers_of_valgard.settler.skill import LEVELS, ODDS

yield_type_arg = Argument("building_type", "the type of building whose yield you want")
def yield_execute(cmd):
    proto = find_object(BuildingPrototype, yield_type_arg.value)
    all = Query(BuildingPrototype).all()

    if proto is None:
        print_error(f'Building Prototype "{color(yield_type_arg.value, Palette.INPUT_COLOR)}" not found')
    
    if isinstance(proto, Harvester):
        for level in LEVELS:
            avg = Bundle()

            for i in range(8):
                avg += ODDS[level.value][i] * proto.basket[i]
            
            print(f'{level}: {avg}')
    else:
        # TODO add yields for non harvesters?
        print_error('Yields from non-harvesters not yet implemented!')
yield_cmd = Command("yield", "find the average yield of a prototype", yield_execute, arguments=[yield_type_arg])