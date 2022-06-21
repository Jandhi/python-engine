import json
from objects.game_object import get_object_types, get_object_pool, squash_ids
from objects.construction import construct
from objects.linking import link_objects
from objects.serialization import serialize

def save_file(file_name):
    pool = get_object_pool()
    types = list(pool.keys())

    for type in types:
        if get_object_types()[type].Schema.is_singleton:
            continue

        squash_ids(type)

    with open(f'{file_name}.json', 'w') as file:
        data = json.dumps(serialize(pool), indent=4)
        file.write(data)

def load_file(file_name):
    with open(f'{file_name}.json', 'r') as file:
        data = json.load(file)
        
        for base_type, objects in data.items():
            if get_object_types()[base_type].Schema.is_singleton:
                construct(objects)
                continue
            
            for id, obj_data in objects.items():
                obj_data['id'] = id
                construct(obj_data)
    
    link_objects()