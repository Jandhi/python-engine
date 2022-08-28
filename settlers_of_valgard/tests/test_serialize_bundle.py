from objects.game_object import find_object, get_object_pool, get_static_pool, initialize_objects
from objects.save_and_load import load_file, save_file
from settlers_of_valgard.resource.resource import Wood
from settlers_of_valgard.settlement import Settlement

s = Settlement()
s.stockpile += Wood * 3
s.stockpile += Wood * 3

save_file('settlers_of_valgard/tests/output/bundle')
load_file('settlers_of_valgard/tests/output/bundle')

stockpile = find_object(Settlement).stockpile

assert(stockpile.count(lambda res : res.resource == Wood) == 6)