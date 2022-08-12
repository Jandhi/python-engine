from noise.dice import roll
from noise.seed import seed

assert(roll(seed() * 'dice', (3, 6)) == [1, 4, 2])