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
    
    def remove(self, resource, amount):
        return self.add(resource ,amount * -1)

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
    
    def __mul__(self, other):
        contents = self.contents.copy()

        for res in contents:
            contents[res] *= other
        
        return Bundle(contents)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        for res in self.contents:
            self.contents[res] *= 2
        
        return self

    def copy(self):
        return Bundle(self.contents.copy())
    
    def __str__(self) -> str:
        s = ''

        for res, amt in self.contents.items():
            s = f'{s}, {amt} {res}'

        if s == '':
            return '-'

        return s[2:]
    
    def first(self):
        for key in self.contents:
            if self.contents[key] > 0:
                return key

def make_bundle(data):
    return Bundle(construct(data['data']))

add_constructor('bundle', make_bundle)