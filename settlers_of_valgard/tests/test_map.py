from settlers_of_valgard.map.map import Map
from objects.save_and_load import save_file, load_file

map = Map(100, 100)

save_file('settlers_of_valgard/tests/output/map')
load_file('settlers_of_valgard/tests/output/map')