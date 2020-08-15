import pygame
import color_constants

def start_screen(WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main, alg_info_screen):
    on_start_screen = True
    padding = WIDTH // 100

    # Creates name text
    name_text = roboto_30.render("Meshan Khosla", 1, color_constants.WHITE)

    # Creates "Pathfinding Visualizer" text
    starting_text_top = roboto_100.render(
        "Pathfinding", 1, color_constants.WHITE)
    starting_text_bottom = roboto_100.render(
        "Visualizer", 1, color_constants.WHITE)

    # Creates instruction text
    instruction_text = roboto_60.render(
        "Instructions", 1, color_constants.WHITE)
    instruction_1_text = roboto_30.render(
        "1. Click which algorithm you want to visualize", 1, color_constants.WHITE)
    instruction_2_text = roboto_30.render(
        "2. Place the start and end position by right clicking on any grid spot", 1, color_constants.WHITE)
    instruction_3_text = roboto_30.render(
        "3. Place any barriers by right clicking/dragging on the grid", 1, color_constants.WHITE)
    instruction_4_text = roboto_30.render(
        "4. Press the space bar to visualize", 1, color_constants.WHITE)
    instruction_5_text = roboto_30.render(
        "If you'd like to try another path after the first one is done, press 'r'", 1, color_constants.WHITE)
    instruction_6_text = roboto_30.render(
        "If you'd like to return to this screen, press the ESC key", 1, color_constants.WHITE)

    # Creates algorithm buttons and position them responsively
    a_star_btn = pygame.Rect(
        padding, WIDTH - (WIDTH // 3) + padding, (WIDTH // 4) - padding - 2, WIDTH // 8)
    bfs_btn = pygame.Rect(a_star_btn.x + a_star_btn.width + (padding),
                          WIDTH - (WIDTH // 3) + padding, (WIDTH // 4) - padding - 2, WIDTH // 8)
    dijkstra_btn = pygame.Rect(bfs_btn.x + bfs_btn.width + (padding), WIDTH - (
        WIDTH // 3) + padding, (WIDTH // 4) - padding - 2, WIDTH // 8)
    dfs_btn = pygame.Rect(dijkstra_btn.x + dijkstra_btn.width + (padding),
                          WIDTH - (WIDTH // 3) + padding, (WIDTH // 4) - padding - 2, WIDTH // 8)

    # Creates algorithm button text
    a_star_text = roboto_60.render("A*", 1, color_constants.WHITE)
    bfs_text = roboto_60.render("BFS", 1, color_constants.WHITE)
    dijkstra_text = roboto_60.render("Dijkstra", 1, color_constants.WHITE)
    dfs_text = roboto_60.render("DFS", 1, color_constants.WHITE)

    # Creates algorithm info button text
    a_star_info_text = roboto_30.render("A*", 1, color_constants.WHITE)
    bfs_info_text = roboto_30.render("BFS", 1, color_constants.WHITE)
    dijkstra_info_text = roboto_30.render("Dijkstra", 1, color_constants.WHITE)
    dfs_info_text = roboto_30.render("DFS", 1, color_constants.WHITE)
    info_text = roboto_30.render("info", 1, color_constants.WHITE)
    while on_start_screen:
        WIN.fill(color_constants.NAVY_BLUE)

        # Draws name text
        WIN.blit(name_text, (WIDTH - name_text.get_width() - padding, padding + 5))

        # Draws "Pathfinding Visualizer" text
        WIN.blit(starting_text_top, ((WIDTH // 2) -
                                     starting_text_top.get_width() // 2, WIDTH // 15))
        WIN.blit(starting_text_bottom, (((WIDTH // 2) - (starting_text_bottom.get_width() // 2)),
                                        (WIDTH // 15) + starting_text_top.get_height() + 15))
        pygame.draw.rect(WIN, color_constants.WHITE, (((WIDTH // 2) - starting_text_top.get_width() // 2) - 15, starting_text_top.get_height() -
                                                      30, starting_text_top.get_width() + 30, starting_text_top.get_height() + starting_text_bottom.get_height() + 30), 3)

        # Draws Instruction text
        WIN.blit(instruction_text, (WIDTH // 2 - (round(name_text.get_width() // 1.5)),
                                    starting_text_top.get_height() + starting_text_bottom.get_height() + name_text.get_height() + 90))
        WIN.blit(instruction_1_text, (15, starting_text_top.get_height(
        ) + starting_text_bottom.get_height() + name_text.get_height() + instruction_text.get_height() + 100))
        WIN.blit(instruction_2_text, (15, starting_text_top.get_height(
        ) + starting_text_bottom.get_height() + name_text.get_height() + instruction_text.get_height() + 140))
        WIN.blit(instruction_3_text, (15, starting_text_top.get_height(
        ) + starting_text_bottom.get_height() + name_text.get_height() + instruction_text.get_height() + 180))
        WIN.blit(instruction_4_text, (15, starting_text_top.get_height(
        ) + starting_text_bottom.get_height() + name_text.get_height() + instruction_text.get_height() + 220))
        WIN.blit(instruction_5_text, (15, starting_text_top.get_height(
        ) + starting_text_bottom.get_height() + name_text.get_height() + instruction_text.get_height() + 260))
        WIN.blit(instruction_6_text, (15, starting_text_top.get_height(
        ) + starting_text_bottom.get_height() + name_text.get_height() + instruction_text.get_height() + 300))

        # Draws Algorithm buttons
        pygame.draw.rect(WIN, color_constants.RED, a_star_btn)
        pygame.draw.rect(WIN, color_constants.TURQUOISE, bfs_btn)
        pygame.draw.rect(WIN, color_constants.BLACK, dijkstra_btn)
        pygame.draw.rect(WIN, color_constants.PURPLE, dfs_btn)

        # Draws Algorithm text on buttons
        WIN.blit(a_star_text, (round(((a_star_btn.x + a_star_btn.width) // 2) -
                                     a_star_text.get_width() // 2), round(a_star_btn.y + a_star_text.get_height() // 1.5)))
        WIN.blit(bfs_text, (round(bfs_btn.x + bfs_text.get_width() //
                                  1.5), round(bfs_btn.y + bfs_text.get_height() // 1.5)))
        WIN.blit(dijkstra_text, (round(dijkstra_btn.x + dijkstra_text.get_width() //
                                       7), round(dijkstra_btn.y + dijkstra_text.get_height() // 1.5)))
        WIN.blit(dfs_text, (round(dfs_btn.x + dfs_text.get_width() //
                                  1.5), round(dfs_btn.y + dfs_text.get_height() // 1.5)))

        # Creates and draws algorithm info buttons
        a_star_info_btn = pygame.draw.circle(WIN, color_constants.WHITE, (
            a_star_btn.x + 100, WIDTH - a_star_btn.height + padding), 50, 2)  # Last parameter is border thickness
        bfs_info_btn = pygame.draw.circle(
            WIN, color_constants.WHITE, (bfs_btn.x + 100, WIDTH - bfs_btn.height + padding), 50, 2)
        dijkstra_info_btn = pygame.draw.circle(WIN, color_constants.WHITE, (
            dijkstra_btn.x + 100, WIDTH - dijkstra_btn.height + padding), 50, 2)
        dfs_info_btn = pygame.draw.circle(
            WIN, color_constants.WHITE, (dfs_btn.x + 100, WIDTH - dfs_btn.height + padding), 50, 2)

        # Draws algorithm info on info buttons
        WIN.blit(a_star_info_text, (a_star_info_btn.x + (a_star_info_text.get_width()) +
                                    (padding * 2), a_star_info_btn.y + (a_star_info_btn.height // 3) - padding))
        WIN.blit(bfs_info_text, (bfs_info_btn.x + bfs_info_text.get_width() -
                                 padding, bfs_info_btn.y + (bfs_info_btn.height // 3) - padding))
        WIN.blit(dijkstra_info_text, (dijkstra_info_btn.x + round(padding * 1.7),
                                      dijkstra_info_btn.y + (dijkstra_info_btn.height // 3) - padding))
        WIN.blit(dfs_info_text, (dfs_info_btn.x + round(padding * 3.5),
                                 dfs_info_btn.y + (dfs_info_btn.height // 3) - padding))
        WIN.blit(info_text, (a_star_info_btn.x + (a_star_info_text.get_width()
                                                  ) + padding, dfs_info_btn.y + (dfs_info_btn.height // 2)))
        WIN.blit(info_text, (bfs_info_btn.x + (bfs_info_text.get_width()
                                               ) - padding, dfs_info_btn.y + (dfs_info_btn.height // 2)))
        WIN.blit(info_text, (dijkstra_info_btn.x + (dijkstra_info_text.get_width()) -
                             round(padding * 5.5), dfs_info_btn.y + (dfs_info_btn.height // 2)))
        WIN.blit(info_text, (dfs_info_btn.x + (dfs_info_text.get_width()
                                               ) - padding, dfs_info_btn.y + (dfs_info_btn.height // 2)))

        # Goes at end of function to avoid not accessed error
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_start_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # Executing algorithm
                if a_star_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    main(WIN, WIDTH, "a_star")
                if bfs_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    main(WIN, WIDTH, "bfs")
                if dijkstra_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    main(WIN, WIDTH, "dijkstra")
                if dfs_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    main(WIN, WIDTH, "dfs")

                # Clicked on info screens
                if a_star_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("A*", WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main)
                if bfs_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("Breadth First Search", WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main)
                if dijkstra_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("Dijkstra", WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main)
                if dfs_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("Depth First Search", WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main)

        pygame.display.update()