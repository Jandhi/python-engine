from noise.munge import hash_string, munge

class Seed:
    def __init__(self, value) -> None:        
        self.value = value
    
    def __mul__(self, other):
        if isinstance(other, Seed):
            return Seed(munge(self.value, other.value))

        if isinstance(other, int):
            return Seed(munge(self.value, other))
        
        if isinstance(other, str):
            return Seed(munge(self.value, hash_string(other)))
        
        if isinstance(other, type):
            return Seed(munge(self.value), hash_string(other.__name__))
        
        raise ValueError(f'Can\'t mix seed with {type(other)}')

    __rmul__ = __mul__

    def at(self, pos):
        return munge(self.value, pos)

__game_seed = Seed(0)

def set_game_seed(val):
    global __game_seed
    __game_seed = val

def get_game_seed():
    return __game_seed

def seed():
    return __game_seed