from objects.game_object import get_object_class, GameObject

def construct(data):
    # string
    if isinstance(data, str):
        try:
            return float(data)
        except ValueError:
            pass

        try:
            return int(data)
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
        obj = cls.__new__(cls)

        for name, value in data.items():
            if name in cls.Schema.do_not_load:
                continue

            obj.__dict__[name] = construct(value)

        GameObject.__init__(obj)
        return obj
    
    # dict
    return {construct(key) : construct(value) for key, value in data.items()}