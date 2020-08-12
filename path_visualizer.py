from os import name
import pygame
import color_constants
from Node import Node
from a_star import run_a_star
from bfs import run_bfs
from dijkstra import run_dijkstra
from dfs import run_dfs
pygame.init()

roboto_100 = pygame.font.SysFont("Roboto", 100)
roboto_60 = pygame.font.SysFont("Roboto", 60)
roboto_30 = pygame.font.SysFont("Roboto", 30)
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding")
    
def main(win, width, alg):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None
    
    run = True
    started = False


    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_coordinates(pos, ROWS, width)
                node = grid[row][col]  # the node/spot that was clicked on
                if not start and node != end:  # Sets start node
                    start = node
                    start.make_start()
                elif not end and node != start:  # Sets end node
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_coordinates(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None
            
            #  Execute algorithm
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end and not started:
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end, alg)
                
                if event.key == pygame.K_r:  # Reset
                    start = None
                    end = None
                    started = False
                    grid = make_grid(ROWS, width)
    pygame.quit()

def algorithm(draw, grid, start, end, alg):
    if alg == "dfs":
        run_dfs(draw, grid, start, end)
    elif alg == "bfs":
        run_bfs(draw, grid, start, end)
    elif alg == "dijkstra":
        run_dijkstra(draw, grid, start, end)
    else:
        run_a_star(draw, grid, start, end)

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
        pygame.draw.line(win, color_constants.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, color_constants.GREY, (j * gap, 0), (j * gap, width))

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



def start_screen():
    on_start_screen = True
    padding = WIDTH // 100

    # Creates algorithm buttons and position them responsively
    a_star_btn = pygame.Rect(padding, WIDTH - (WIDTH // 3), (WIDTH // 4) - padding - 2, WIDTH // 8)
    bfs_btn = pygame.Rect(a_star_btn.x + a_star_btn.width + (padding), WIDTH - (WIDTH // 3), (WIDTH // 4) - padding - 2, WIDTH // 8)
    dijkstra_btn = pygame.Rect(bfs_btn.x + bfs_btn.width + (padding), WIDTH - (WIDTH // 3), (WIDTH // 4) - padding - 2, WIDTH // 8)
    dfs_btn = pygame.Rect(dijkstra_btn.x + dijkstra_btn.width + (padding), WIDTH - (WIDTH // 3), (WIDTH // 4) - padding - 2, WIDTH // 8)
    
    # Creates algorithm button text
    a_star_text = roboto_60.render("A*", 1, color_constants.WHITE)
    bfs_text = roboto_60.render("BFS", 1, color_constants.WHITE)
    dijkstra_text = roboto_60.render("Dijkstra", 1, color_constants.WHITE)
    dfs_text = roboto_60.render("DFS", 1, color_constants.WHITE)

    # Creates "Pathfinding Visualizer" text
    starting_text_top = roboto_100.render("Pathfinding", 1, color_constants.WHITE)
    starting_text_bottom = roboto_100.render("Visualizer", 1, color_constants.WHITE)

    # Creates name text
    name_text = roboto_30.render("By: Meshan Khosla", 1, color_constants.WHITE)

    while on_start_screen:
        WIN.fill(color_constants.NAVY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_start_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
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


        # Draws "Pathfinding Visualizer" text
        WIN.blit(starting_text_top, ((WIDTH // 2) - starting_text_top.get_width() // 2, WIDTH // 15))
        WIN.blit(starting_text_bottom, (((WIDTH // 2 ) - (starting_text_bottom.get_width() // 2)), (WIDTH // 15) + starting_text_top.get_height() + 15))
        
        # Draws name text
        WIN.blit(name_text, (WIDTH // 2 - name_text.get_width() // 2, (WIDTH // 15) + starting_text_top.get_height() + starting_text_bottom.get_height() + 25))

        # Draws Algorithm buttons
        pygame.draw.rect(WIN, color_constants.RED, a_star_btn)
        pygame.draw.rect(WIN, color_constants.TURQUOISE, bfs_btn)
        pygame.draw.rect(WIN, color_constants.BLACK, dijkstra_btn)
        pygame.draw.rect(WIN, color_constants.PURPLE, dfs_btn)

        # Draws Algorithm text on buttons
        WIN.blit(a_star_text, (round(((a_star_btn.x + a_star_btn.width) // 2) - a_star_text.get_width() // 2), round(a_star_btn.y + a_star_text.get_height() // 1.5)))
        WIN.blit(bfs_text, (round(bfs_btn.x + bfs_text.get_width() // 1.5), round(bfs_btn.y + bfs_text.get_height() // 1.5)))
        WIN.blit(dijkstra_text, (round(dijkstra_btn.x + dijkstra_text.get_width() // 7), round(dijkstra_btn.y + dijkstra_text.get_height() // 1.5)))
        WIN.blit(dfs_text, (round(dfs_btn.x + dfs_text.get_width() // 1.5), round(dfs_btn.y + dfs_text.get_height() // 1.5)))

        pygame.display.update()
        """
        Instructions: 
        1. Click which algorithm you want to visualize
        2. Place the start and end position by right clicking on any grid spot
        3. Place any barriers by right click/dragging on the grid
        4. Press the space bar
        If you'd like to try another visualization after the first one is done, press 'r'
        If you'd like to return to this screen, press the ESC key
        """

start_screen()