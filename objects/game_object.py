import re
from typing import Callable
from console.colored_object import ColoredObject

from objects.serialization import serialize_field

camel_to_snake = re.compile(r'(?<!^)(?=[A-Z])')

__id_counter = {}
__object_pool : dict[str, dict[id,]] = {}
__static_pool : dict[str, dict[id,]] = {}
__object_types = {}
__static_types = {}
__deletion_pool = []

LINK_STRING = '-> '

def initialize_objects():
    global __id_counter, __object_pool, __object_types, __deletion_pool

    __id_counter = {}
    __object_pool = {}
    __object_types = {}
    __deletion_pool = []

def get_object_types():
    return __object_types

def get_object_pool():
    return __object_pool

def delete_game_object(item):
    item.deleted = True
    __deletion_pool.append(item)

def clear_deletion_pool():
    global __deletion_pool

    for item in __deletion_pool:
        del item
    
    __deletion_pool = []

def initialize_type(type):
    __object_pool[type] = {}

    if not __object_types[type].Schema.is_singleton:
        __id_counter[type] = 0
    
    if __object_types[type].Schema.is_static:
        __static_pool[type] = __object_pool[type]

def squash_ids(type):
    objects = list(__object_pool[type].values())
    __object_pool[type] = {}
    for id, object in enumerate(objects):
        object.id = id
        __object_pool[type][id] = object
    
    __id_counter[type] = len(objects)

def add_object_singleton(game_object):
    __object_pool[game_object.type] = game_object

def add_object(game_object):
    base_type = game_object.base_type

    if base_type not in __object_pool:
        initialize_type(base_type)

    if game_object.id is None:
        game_object.id = __id_counter[base_type]
        __id_counter[base_type] += 1
    
    __object_pool[base_type][game_object.id] = game_object

def remove_object(game_object):
    type = game_object.type

    if type in __object_types and __object_types[type].Schema.is_singular:
        return __object_pool.pop(type) 

    base_type = game_object.base_type
    __object_pool[base_type].pop(game_object.id)

def get_base_type(type):
    if type not in __object_types:
        return None

    return __object_types[type].base_type

def find_object(type_name, id = None):
    if isinstance(type_name, type):
        type_name = type_name.type
    else:
        type_name = type_name.lower()

    if type_name in __object_types and __object_types[type_name].Schema.is_singleton:
        return __object_pool[type_name]

    base_type = get_base_type(type_name)

    if base_type not in __object_pool:
        return None
    
    if id not in __object_pool[base_type]:
        return None
    
    return __object_pool[base_type][id]

def get_objects(type):
    base_type = get_base_type(type)

    if not base_type in __object_pool:
        return []

    return list(__object_pool[base_type].values())

def add_type(cls):
    __object_types[cls.type] = cls

def add_static_type(cls):
    __static_types[cls.type] = cls

def remove_static_objects():
    for type in __static_pool:
        __object_pool.pop(type)

def add_static_objects():
    for type, objects in __static_pool.items():
        __object_pool[type] = objects

def get_object_class(type):
    if type not in __object_types:
        return None
    
    return __object_types[type]

class GameObjectMeta(type):
    def __new__(meta, name, bases, dct):
        class_ = super(GameObjectMeta, meta).__new__(meta, name, bases, dct)
        
        if 'type' not in dct:
            class_.type = camel_to_snake.sub('_', name).lower()

        if not class_.base_type and class_.type != 'game_object':
            class_.base_type = class_.type

        add_type(class_)

        if class_.Schema.is_singleton:
            obj = class_.make_instance(class_)
            GameObject.__init__(obj)

        if class_.Schema.is_static:
            add_static_type(class_)

        return class_

class GameObject(ColoredObject, metaclass=GameObjectMeta):
    type : str = None
    base_type : str = None
    
    class Schema:
        first_fields = ['type']
        do_not_serialize = ['id', 'deleted']
        do_not_load = ['deleted']
        constructors = {}
        is_singleton = False
        is_static = False
        class_fields = []
        numeric_id = True

    def __init__(self) -> None:
        self.deleted = False

        if self.Schema.is_singleton:
            return add_object_singleton(self)

        if 'id' not in self.__dict__:
            self.id = None
        add_object(self)

    def __serialize__(self) -> dict:
        data = {}

        if self.Schema.first_fields:
            for field in self.Schema.first_fields:
                data[field] = serialize_field(getattr(self, field))

        for name, value in self.__dict__.items():
            if name in data or name in self.Schema.do_not_serialize:
                continue

            data[name] = serialize_field(value)

        for name, value in type(self).__dict__.items():
            if name in self.Schema.class_fields or \
                (self.Schema.is_singleton and not name.startswith('__') and not isinstance(value, Callable)):
                data[name] = serialize_field(value)

        delete_game_object(self)
        
        return data

    def __serialize_field__(self) -> str:
        if self.Schema.is_singleton:
            return f'{LINK_STRING}type : {self.type}'

        return f'{LINK_STRING}type : {self.type}, id : {self.id}'