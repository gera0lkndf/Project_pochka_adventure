import pygame
from mail import WIN_WIDTH, WIN_HEIGHT, main
from settings import load_image

pygame.init()
size = (WIN_WIDTH, WIN_HEIGHT)
screen = pygame.display.set_mode(size)

color_text = (31, 52, 56)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Times New Roman', 60)


def level_selection():
    lavel_select = True
    while lavel_select:
        screen.fill((89, 25, 60))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lavel_select = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 750 <= mouse[0] <= width / 2 - 450 and height // 2 - 145 <= mouse[1] <= height // 2 + 145:
                    main(0)
                if width / 2 - 348 <= mouse[0] <= width / 2 - 52 and height // 2 - 145 <= mouse[1] <= height // 2 + 145:
                    main(1)
                if width / 2 + 52 <= mouse[0] <= width / 2 + 348 and height // 2 - 145 <= mouse[1] <= height // 2 + 145:
                    main(2)

        # фон
        fon = pygame.transform.scale(load_image('fons.jpg'), (WIN_WIDTH, WIN_HEIGHT))
        screen.blit(fon, (0, 0))

        # создание табличек выбора уровня
        tables_levels = pygame.image.load("data/table_levels.png")
        chains = pygame.image.load("data/chains_lvl.png")
        table_width = WIN_WIDTH // 2 - 600
        for i in range(4):
            rect = tables_levels.get_rect(center=(table_width, WIN_HEIGHT // 2))
            screen.blit(tables_levels, rect)
            table_width += 400
        rect_lvl = tables_levels.get_rect(center=(table_width - 400, WIN_HEIGHT // 2 - 10))
        screen.blit(chains, rect_lvl)

        # создание номера уровня
        text_width = WIN_WIDTH // 2 - 620
        for i in range(1, 4):
            num = str(i)
            number_lvl = smallfont.render(num, True, color_text)
            screen.blit(number_lvl, (text_width, WIN_HEIGHT // 2 - 30))
            text_width += 405

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    level_selection()
