def serialize(object):
    if hasattr(object, '__serialize__'):
        return object.__serialize__()
    elif isinstance(object, list) or isinstance(object, set):
        return [serialize(item) for item in object]
    elif isinstance(object, dict):
        return {serialize_field(key) : serialize(value) for key, value in object.items()}
    else:
        return str(object)
    

def serialize_field(object):
    if hasattr(object, '__serialize_field__'):
        return object.__serialize_field__()
    elif isinstance(object, list) or isinstance(object, set):
        return [serialize_field(item) for item in object]
    elif isinstance(object, dict):
        return {serialize_field(key) : serialize_field(value) for key, value in object.items()}
    else:
        return serialize(object)