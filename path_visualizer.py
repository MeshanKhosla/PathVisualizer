import pygame
import color_constants
from Node import Node
from a_star import run_a_star
from bfs import run_bfs
from dijkstra import run_dijkstra
from dfs import run_dfs
from alg_info import info

pygame.init()

roboto_100 = pygame.font.SysFont("Roboto", 100)
roboto_60 = pygame.font.SysFont("Roboto", 60)
roboto_30 = pygame.font.SysFont("Roboto", 30)
roboto_25 = pygame.font.SysFont("Roboto", 25)
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding")


def reconstruct_path(parent, current, draw):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    while current in parent:
        current = parent[current]   # Goes backwards until start node
        if current:
            current.make_path()
        draw()


def main(win, width, alg):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start_node = None
    end_node = None

    running = True
    started = False

    while running:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_coordinates(pos, ROWS, width)
                node = grid[row][col]  # the node/spot that was clicked on
                if not start_node and node != end_node:  # Sets start_node node
                    start_node = node
                    start_node.make_start()
                elif not end_node and node != start_node:  # Sets end_node node
                    end_node = node
                    end_node.make_end()
                elif node != end_node and node != start_node:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_coordinates(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start_node:
                    start_node = None
                if node == end_node:
                    end_node = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node and end_node and not started:  # Execute algorithm
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start_node, end_node, alg)

                if event.key == pygame.K_r:  # Reset
                    start_node = None
                    end_node = None
                    started = False
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_ESCAPE:  # Return to start screen
                    running = False
                    start_screen()
    pygame.quit()


def algorithm(draw, grid, start, end, alg):
    if alg == "dfs":
        run_dfs(draw, grid, start, end, reconstruct_path)
    elif alg == "bfs":
        run_bfs(draw, grid, start, end, reconstruct_path)
    elif alg == "dijkstra":
        run_dijkstra(draw, grid, start, end, reconstruct_path)
    else:
        run_a_star(draw, grid, start, end, reconstruct_path)

# Creates 2D array for grid


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

# Draws grid lines


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, color_constants.GREY,
                         (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, color_constants.GREY,
                             (j * gap, 0), (j * gap, width))

# Actually draws the nodes onto the screen


def draw(win, grid, rows, width):
    win.fill(color_constants.WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


"""
Returns the coordinate that mouse was clicked in
ie: center is 400, 400
return: 25, 25 on a 50x50 grid
"""


def get_clicked_coordinates(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col


def alg_info_screen(alg):
    on_alg_info_screen = True

    # Creates back button and title text
    back_arrow = pygame.image.load('./assets/arrow.png')
    alg_title_text = roboto_100.render(alg, 1, color_constants.WHITE)
    

    while on_alg_info_screen:
        WIN.fill(color_constants.CHARCOAL_GREY)
        # Draws back button and text
        WIN.blit(back_arrow, (5, 5))
        WIN.blit(alg_title_text, ((WIDTH // 2) - alg_title_text.get_width() // 2, WIDTH // 15))

        # Loops through every line of info b/c pygame doesn't have multiline support :(
        cur_height = WIDTH // 5
        for i in range(1, len(info[alg]) + 1):
            alg_info_text = roboto_25.render(info[alg][i], 1, color_constants.WHITE)
            WIN.blit(alg_info_text, (15, cur_height))
            cur_height += 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_alg_info_screen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_arrow.get_rect().collidepoint(mouse_pos):
                    on_alg_info_screen = False
                    start_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Return to start screen
                    on_alg_info_screen = False
                    start_screen()

        pygame.display.update()


def start_screen():
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
                    alg_info_screen("A*")
                if bfs_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("Breadth First Search")
                if dijkstra_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("Dijkstra")
                if dfs_info_btn.collidepoint(mouse_pos):
                    on_start_screen = False
                    alg_info_screen("Depth First Search")

        pygame.display.update()


start_screen()
