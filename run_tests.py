

from noise.dice import highest
from noise.seed import Seed, get_game_seed
from objects.game_object import get_static_pool
from objects.static_object import list_statics

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

list_statics()