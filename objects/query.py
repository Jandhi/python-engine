from objects.game_object import GameObject, get_objects

CONTAINS = 'contains'
STARTS_WITH = 'starts_with'
ENDS_WITH = 'ends_with'

def match(obj, value, pattern):
    if pattern == CONTAINS:
        return any([match(item, value) for item in obj])
    
    if hasattr(obj, 'name'):
        return match(obj.name, value, pattern)

    if isinstance(value, str):
        value = value.lower()
        obj = obj.lower()

    if pattern == STARTS_WITH:
        return obj.startswith(value)
    
    if pattern == ENDS_WITH:
        return obj.endswith(value)

    if pattern == None:
        return obj == value

class Query():
    def __init__(self, query_type) -> None:
        self.query_type = query_type
        self.objects : list = get_objects(query_type)

    def with_field(self, name, value, pattern = None):
        def fltr(obj : GameObject):
            if not hasattr(obj, name):
                return False

            return match(getattr(obj, name), value, pattern)

        self.objects = list(filter(fltr, self.objects))

        return self
    
    def first(self):
        if len(self.objects) > 0:
            return self.objects[0]
        else:
            return None
    
    def all(self):
        return self.objects