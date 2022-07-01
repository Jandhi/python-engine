

from objects.game_object import get_static_pool
from objects.static_object import list_statics
from settlers_of_valgard.colors import print_256colors, print_colors
import tests.test_event
import tests.test_cprint
import tests.test_event_parents
import tests.test_colored_names
import tests.test_save_and_load
import tests.test_singleton
import tests.test_serializeable
import tests.test_static_objects

import settlers_of_valgard.tests.run_tests
import settlers_of_valgard.rank

print_colors()

list_statics()