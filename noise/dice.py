from noise.seed import Seed

class DicePool:
    def __init__(self, *dice) -> None:
        self.contents = {faces : amt for (amt, faces) in dice}
    
    def roll(self, seed):
        return roll(seed, *((amt, faces) for faces, amt in self.contents.items()))
    
    def highest(self, seed):
        return max(self.roll(seed))

    def __add_pool__(self, pool):
        contents = self.contents.copy()

        for faces, amt in pool.contents.items():
            if faces in contents:
                contents[faces] += amt
            else:
                contents[faces] = amt
        
        pool = DicePool()
        pool.contents = contents
        return pool
    
    def __add__(self, other):
        if isinstance(other, DicePool):
            return self.__add_pool__(other)
        
        if isinstance(other, tuple):
            amt, faces = other

            

    def __iadd__(self, other):
        for faces, amt in other.contents.items():
            if faces in self.contents:
                self.contents[faces] += amt
            else:
                self.contents[faces] = amt
        
        return self


def roll(seed : Seed, *dice):
    rolled = []
    counter = 0
    
    for (amt, faces) in dice:
        for i in range(amt):
            rolled.append(seed.at(counter) % faces + 1)
            counter += 1
    
    return rolled

def highest(seed : Seed, *dice):
    return max(roll(seed, *dice))