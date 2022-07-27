from objects.game_object import GameObject, get_objects

CONTAINS = 'contains'
STARTS_WITH = 'starts_with'
ENDS_WITH = 'ends_with'

def match(obj, value, pattern):
    if isinstance(obj, str):
        value = value.lower()
        obj = obj.lower()

    if isinstance(pattern, tuple) and pattern[0] == CONTAINS:
        return any([match(item, value, list(pattern)[1:]) for item in obj])

    if pattern == CONTAINS:
        return value in obj
    
    if hasattr(obj, 'name'):
        return match(obj.name, value, pattern)

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

    def filter(self, fltr):
        self.objects = list(filter(fltr, self.objects))

        return self
    
    def first(self):
        if len(self.objects) > 0:
            return self.objects[0]
        else:
            return None
    
    def all(self):
        return self.objects
    
    def count(self):
        return len(self.objects)