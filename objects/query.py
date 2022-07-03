from objects.game_object import GameObject, get_objects

def match(obj, value, pattern):
    pass

class Query():
    def __init__(self, query_type) -> None:
        self.query_type = query_type
        self.objects = get_objects(query_type)

    def with_field(self, name, value, pattern = None):
        def fltr(obj : GameObject):
            if not hasattr(obj, name):
                return False

            return match(getattr(obj, name), value, pattern)

        self.objects = list(filter(fltr, self.object))

        return self