from objects.game_object import get_object_class, GameObject

__constructors = {}

def add_constructor(name, constructor):
    __constructors[name] = constructor

def construct(data):
    # numbers
    if isinstance(data, int) or isinstance(data, float):
        return data

    # string
    if isinstance(data, str):
        try:
            return int(data)
        except ValueError:
            pass

        try:
            return float(data)
        except ValueError:
            pass

        return data
    
    # list
    if isinstance(data, list):
        return [construct(item) for item in data]

    # pointer
    if data.keys() == ['type', 'id']:
        return data

    if 'type' in data:
        cls = get_object_class(data['type'])
        
        if cls is not None:
            return construct_game_object(cls, data)
        
        if data['type'] in __constructors:
            return __constructors[data['type']](data)
    
    # dict
    return {construct(key) : construct(value) for key, value in data.items()}

def construct_game_object(cls, data):
    schema : GameObject.Schema = cls.Schema
    obj : GameObject = cls.__new__(cls)

    for name, value in data.items():
        if name in schema.do_not_load:
            continue

        if name in schema.class_fields:
            setattr(cls, name, construct(value))
            continue

        constructed = construct(value)
        setattr(obj, name, constructed)

    GameObject.__init__(obj)

    obj.post_construction()    
    
    return obj