import sys
import os
from pygame.image import load

width, height = size = 1920, 1025

SCREEN_WIDTH = width
SCREEN_HEIGHT = 945

tile_width = tile_height = 50

GRAVITY = 1


def load_image(name, colorkey=None):
    fullname = os.path.join('data/', name)
    if not os.path.isfile(fullname):
        print('Not file')
        sys.exit()
    image = load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
