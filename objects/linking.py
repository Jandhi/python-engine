from objects.game_object import find_object, get_object_pool, get_object_types, LINK_STRING

def link(obj):
    if obj is None:
        return obj

    if isinstance(obj, str):
        if obj.startswith(f'{LINK_STRING}type :'):
            id_index = obj.find(', id :')

            if id_index == -1: # singleton case
                return find_object(obj[7 + len(LINK_STRING):])

            type = obj[7 + len(LINK_STRING) : id_index]
            id = obj[id_index + 7:] if id_index != -1 else None

            try:
                id = int(id)
            except ValueError:
                pass

            return find_object(type, id)
        else:
            return obj

    if isinstance(obj, list):
        return [link(item) for item in obj]

    if isinstance(obj, dict):
        return {link(key) : link(value) for key, value in obj.items()}

    if isinstance(obj, int) or isinstance(obj, float):
        return obj

    if hasattr(obj, '__link__'):
        obj.__link__()

    keys = obj.__dict__.keys()

    for key in keys:
        obj.__dict__[key] = link(obj.__dict__[key])
    
    return obj

def link_objects():
    pool = get_object_pool()
    for type in pool:
        if get_object_types()[type].Schema.is_singleton:
            link(pool[type])
        else:
            for obj in pool[type].values():
                link(obj)
    
    __linked_objects = []