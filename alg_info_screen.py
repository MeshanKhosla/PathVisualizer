

import pygame
import color_constants
from alg_info import info
from start_screen import start_screen

def alg_info_screen(alg, WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main):
    on_alg_info_screen = True

    # Creates back button and title text
    back_arrow = pygame.image.load('./assets/arrow.png')
    alg_title_text = roboto_100.render(alg, 1, color_constants.WHITE)

    # Images
    if alg == "A*":
        image_one = pygame.image.load('./assets/a_star_1.png')
        image_two = pygame.image.load('./assets/a_star_2.png')
    elif alg == "Breadth First Search":
        image_one = pygame.image.load('./assets/bfs_1.png')
        image_two = pygame.image.load('./assets/bfs_2.png')
    elif alg == "Dijkstra":
        image_one = pygame.image.load('./assets/dijkstra_1.png')
        image_two = pygame.image.load('./assets/dijkstra_2.png')
    else:
        image_one = pygame.image.load('./assets/dfs_1.png')
        image_two = pygame.image.load('./assets/dfs_2.png')
    image_one = pygame.transform.scale(image_one, (350, 300))
    image_two = pygame.transform.scale(image_two, (350, 300))


    while on_alg_info_screen:
        WIN.fill(color_constants.CHARCOAL_GREY)
        # Draws back button and text
        WIN.blit(back_arrow, (5, 5))
        WIN.blit(alg_title_text, ((WIDTH // 2) - alg_title_text.get_width() // 2, WIDTH // 15))

        # Loops through every line of info b/c pygame doesn't have multi-line support :(
        cur_height = WIDTH // 5
        for i in range(1, len(info[alg]) + 1):
            alg_info_text = roboto_25.render(info[alg][i], 1, color_constants.WHITE)
            WIN.blit(alg_info_text, (15, cur_height))
            cur_height += 25

        # Draws images
        WIN.blit(image_one, (15, WIDTH  - image_one.get_height() - 15))
        WIN.blit(image_two, (WIDTH - image_two.get_width() - 15, WIDTH  - image_one.get_height() - 15))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_alg_info_screen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_arrow.get_rect().collidepoint(mouse_pos):
                    on_alg_info_screen = False
                    start_screen(WIN, WIDTH, roboto_30, roboto_25, roboto_60, roboto_100, main, alg_info_screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Return to start screen
                    on_alg_info_screen = False
                    start_screen(WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main, alg_info_screen)

        pygame.display.update()