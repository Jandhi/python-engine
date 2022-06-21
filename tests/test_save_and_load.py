from objects.game_object import GameObject, find_object, initialize_objects
from objects.save_and_load import load_file, save_file

initialize_objects()

class NPC(GameObject):
    type = 'npc'

    def __init__(self, name) -> None:
        super().__init__()

        self.name = name

class SpecialNPC(NPC):
    type = 'special_npc'

    def __init__(self, name, bonds) -> None:
        super().__init__(name)
        self.bonds = bonds

class FavouriteNPC(SpecialNPC):
    type = 'favourite_npc'

    class Schema(SpecialNPC.Schema):
        is_singleton = True

j = SpecialNPC('jan', [])
n = SpecialNPC('nicole', [j])
m = FavouriteNPC('favourite', [j])

j.bonds = [n, m]


save_file('test')
load_file('test')

j = find_object(SpecialNPC.type, 0)

assert(j.bonds[1].bonds[0].name == "jan")