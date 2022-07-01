import re
from objects.construction import add_constructor, construct
from objects.serialization import serialize

class Bundle:
    def __init__(self, contents = None) -> None:
        self.contents = contents or {}
    
    def add(self, resource, amount):
        if resource in self.contents:
            self.contents[resource] += amount
        else:
            self.contents[resource] = amount

    def __serialize__(self):
        return {'type' : 'bundle', 'data' : serialize(self.contents)}
    
    def __add__(self, other):
        return Bundle(self.contents.copy()).__iadd__(other)
    
    def __iadd__(self, other):
        if isinstance(other, Bundle):
            for res, amt in other.contents.items():
                self.add(res, amt)
            
            return self
        
        if isinstance(other, tuple):
            self.add(*other)

            return self
        
        raise ValueError("Can only add bundle or tuple to bundle")

def make_bundle(data):
    return Bundle(construct(data['data']))

add_constructor('bundle', make_bundle)