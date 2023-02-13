# mail файл, тут все собрано, камера, уровень и тд, если хочешь то я перенесу уровни в отдельный файл

import pygame
from player import *
from blocks import *
from level_selection import spisok

WIN_WIDTH = 1920
WIN_HEIGHT = 1025
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#00bfff"


# камера, которая будет следить за персонажем
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


# еще немного про камеру
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


# основа основы, тут и лвл, и названия, и окно, и перемещения и даже основной цикл
def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Great pochka adventure")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    left = right = False
    up = False
    low = False

    entities = pygame.sprite.Group()
    platforms = []

    entities.add(hero)


    level1 = [
        "---------------------------------------------------------------------------",
        "-            --                            -                              -",
        "-                                          -                              -",
        "---                     --                 -                   ------------",
        "-    ---                                   -                              -",
        "-            --                            -                              -",
        "-                                          -                              -",
        "--                                         -                              -",
        "-                                          -     ---------                -",
        "-                   ----     ---           -              -               -",
        "-                                          -                              -",
        "--         ----                            -                             --",
        "-                                          -                              -",
        "-                            ---           -                              -",
        "-                                          -                              -",
        "-                                          -                 ---------    -",
        "-      ---                                 -                              -",
        "-                                                                         -",
        "-                                                                        --",
        "-                                          -          -----               -",
        "-                         -                -                              -",
        "-                            --            -                    ----  -----",
        "-             -----                        -                              -",
        "-                                          -                              -",
        "-                                          -                              -",
        "-                                          -                              -",
        "-            --                            -                              -",
        "-           - -                            -                              -",
        "-             -                            -                              -",
        "-             -                            -                              -",
        "-                                          -                              -",
        "---------------------------------------------------------------------------"]

    level2 = [
        "---------------------------------------------------------------------------",
        "-            --                            -                              -",
        "-                                          -                              -",
        "---                     --                 -                   ------------",
        "-    ---                                   -                              -",
        "-            --                            -                              -",
        "-                                          -                              -",
        "--                                         -                              -",
        "-                                          -     ---------                -",
        "-                   ----     ---           -              -               -",
        "-                                          -                              -",
        "--         ----                            -                             --",
        "-                                          -                              -",
        "-                            ---           -                              -",
        "-                                          -                              -",
        "-                                          -                 ---------    -",
        "-      ---                                 -                              -",
        "-                                                                         -",
        "-                                                                        --",
        "-                                          -          -----               -",
        "-                         -                -                              -",
        "-                            --            -                    ----  -----",
        "-             -----                        -                              -",
        "-                                          -                              -",
        "-                                          -                              -",
        "-              ---                         -                              -",
        "-             -   -                        -                              -",
        "-                 -                        -                              -",
        "-              ---                         -                              -",
        "-             -                           -                              -",
        "-              ----                        -                              -",
        "---------------------------------------------------------------------------"]

    level3 = [
        "---------------------------------------------------------------------------",
        "-            --                            -                              -",
        "-                                          -                              -",
        "---                     --                 -                   ------------",
        "-    ---                                   -                              -",
        "-            --                            -                              -",
        "-                                          -                              -",
        "--                                         -                              -",
        "-                                          -     ---------                -",
        "-                   ----     ---           -              -               -",
        "-                                          -                              -",
        "--         ----                            -                             --",
        "-                                          -                              -",
        "-                            ---           -                              -",
        "-                                          -                              -",
        "-                                          -                 ---------    -",
        "-      ---                                 -                              -",
        "-                                                                         -",
        "-                                                                        --",
        "-                                          -          -----               -",
        "-                         -                -                              -",
        "-                            --            -                    ----  -----",
        "-             -----                        -                              -",
        "-                                          -                              -",
        "-                                          -                              -",
        "-                                          -                              -",
        "-           ---                            -                              -",
        "-             -                            -                              -",
        "-            -                             -                              -",
        "-             -                            -                              -",
        "-           ---                            -                              -",
        "---------------------------------------------------------------------------"]


    timer = pygame.time.Clock()
    x = y = 0

    for row in level1:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            # планировал добавить шипы, пока не дошли руки
            if col == "x":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level1[0]) * PLATFORM_WIDTH
    total_level_height = len(level1) * PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    # основной цикл
    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_w:
                up = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True
            if e.type == KEYUP and e.key == K_w:
                up = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False
            # это функции уменьшения, нерабочие
            if e.type == KEYDOWN and e.key == K_TAB:
                low = True
            if e.type == KEYUP and e.key == K_TAB:
                low = False
            if e.type == KEYDOWN and e.key == K_q:
                small = True

        screen.blit(bg, (0, 0))
        camera.update(hero)
        hero.update(left, right, up, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

# if __name__ == "__main__":
# main()
