from objects.construction import add_constructor, construct
from objects.serialization import serialize

class Bundle:
    def __init__(self, *contents) -> None:
        self.contents : list = list(contents) or []
    
    def add(self, resource):
        for other in self.contents:
            if other.is_stackable(resource):
                other.amount += resource.amount
                return
        
        self.contents.append(resource)
    
    def remove(self, resource, amount):
        removals : list[tuple] = []
        b_contents = []

        for res in self.contents:
            if not res.is_stackable(resource):
                continue
            
            # resource has more than needed
            if res.amount > amount: 
                removals.append((res, amount))
                amount = 0
                break
            # resource has equal or less than needed
            else:
                removals.append((res, res.amount))
                amount -= res.amount
            
            # finished
            if amount == 0:
                break

        if amount > 0:
            return None
        
        for res, amt in removals:
            if res.amount > amt:
                b_contents.append(res.split_off(amt))
            else:
                self.contents.remove(res)
                b_contents.append(res)

        return Bundle(*b_contents)

    def count(self, condition):
        amt = 0

        for res in self.contents:
            if condition(res):
                amt += res.amount
        
        return amt

    def __serialize__(self):
        return {'type' : 'bundle', 'contents' : serialize(self.contents)}
    
    def __add__(self, other):
        return Bundle(*self.contents.copy()).__iadd__(other)
    
    def __iadd__(self, other):
        if isinstance(other, Bundle):
            for res in other.contents:
                self.add(res)
            
            return self
        
        self.add(other)
        return self
    
    def __mul__(self, other):
        contents = [res.copy() for res in self.contents]

        for res in contents:
            res.amount *= other
        
        return Bundle(*contents)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        for res in self.contents:
            res.amount *= other
        
        return self

    def copy(self):
        return Bundle(*self.contents.copy())
    
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
    return Bundle(*construct(data['contents']))

add_constructor('bundle', make_bundle)