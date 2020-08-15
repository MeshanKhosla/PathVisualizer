import pygame
import color_constants
from Node import Node
from a_star import run_a_star
from bfs import run_bfs
from dijkstra import run_dijkstra
from dfs import run_dfs
from alg_info import info
from start_screen import start_screen
from alg_info_screen import alg_info_screen

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
                    start_screen(WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main, alg_info_screen)
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


start_screen(WIN, WIDTH, roboto_25, roboto_30, roboto_60, roboto_100, main, alg_info_screen)

