from noise.munge import munge

class Seed:
    def __init__(self, value) -> None:        
        self.value = hash(value)
    
    def __mul__(self, other):
        if isinstance(other, Seed):
            return Seed(munge(self.value, other.value))

        return Seed(munge(self.value, other))

    __rmul__ = __mul__

    def at(self, pos):
        return munge(self.value, pos)

__game_seed = Seed(0)

def set_game_seed(val):
    global __game_seed
    __game_seed = val

def get_game_seed():
    return __game_seed