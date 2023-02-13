import pygame
from mail import WIN_WIDTH, WIN_HEIGHT, main
from settings import load_image
from level_selection import level_selection

pygame.init()
size = (WIN_WIDTH, WIN_HEIGHT)
screen = pygame.display.set_mode(size)

color_text = (31, 52, 56)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Times New Roman', 60)
text_play = smallfont.render('play', True, color_text)
text_settings = smallfont.render('settings', True, color_text)
text_quit = smallfont.render('quit', True, color_text)


def p_play():
    level_selection()


def p_settings():
    print('settings')


def p_quit():
    quit()


def main_screensaver():
    screensaver = True
    while screensaver:
        screen.fill((89, 25, 60))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screensaver = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 - 156 <= mouse[1] <= height / 2 - 50:
                    p_play()
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 - 36 <= mouse[1] <= height / 2 + 70:
                    pass
                if width / 2 - 140 <= mouse[0] <= width / 2 + 140 and height / 2 + 84 <= mouse[1] <= height / 2 + 190:
                    p_quit()

        # фон главного меню
        fon = pygame.transform.scale(load_image('fons.jpg'), (WIN_WIDTH, WIN_HEIGHT))
        screen.blit(fon, (0, 0))

        # создание 3 табличек на экране главного меню
        tables = pygame.image.load("data/table.png")
        table_height = 410
        for i in range(3):
            rect = tables.get_rect(center=(WIN_WIDTH // 2, table_height))
            screen.blit(tables, rect)
            table_height += 120

        screen.blit(text_play, (width / 2 - 50, height / 2 - 140))
        screen.blit(text_settings, (width / 2 - 93, height / 2 - 22))
        screen.blit(text_quit, (width / 2 - 50, height / 2 + 100))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main_screensaver()
