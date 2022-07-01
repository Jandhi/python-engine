from console.colored_string import color

colors = {}

class Colors:
    # Browns
    WOOD = 94
    FUR = 95

    # Greens
    GRASS = 10
    LIME = 46
    PINE = 22
    SWAMP = 100

    # Reds
    CRIMSON = 124
    RED = 196
    CHERRY = 88

    # Blues
    OCEAN = 21
    LAKE = 33
    WATER = 45
    RIVER = 50
    SKY = 81
    CRYSTAL = 159

    # Purples
    LAVENDER = 147
    MAGENTA = 126
    DEEP_PURPLE = 57

    # Yellows
    LEMON = 190
    SUNSHINE = 226
    GOLD = 178

    # Neutrals
    WHITE = 255
    STONE = 243
    STEEL = 249

def print_256colors():
    s = ''
    for c in range(256):
        t = color(f'COLOR{c}', c)
        s = f'{s} {t}'
    print(s)

def print_colors():
    s = ''
    for name in Colors.__dict__:
        if name.startswith('__'):
            continue

        c = getattr(Colors, name)

        t = color(f'{name}{c}', c)
        s = f'{s} {t}'
    print(s)