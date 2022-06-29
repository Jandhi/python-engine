from objects.game_object import find_object, initialize_objects
from objects.singleton import Singleton
from objects.save_and_load import load_file, save_file

initialize_objects()

class Test(Singleton):
    test = 'test'

    class Schema(Singleton.Schema):
        class_fields = ['test']

obj = find_object('Test') 
Test.test = 'bozo'
assert(obj is not None)

save_file('tests/output/singleton_test')
load_file('tests/output/singleton_test')

obj = find_object('Test')
assert(obj is not None)