import pygame
import color_constants
from Node import Node
from a_star import run_a_star
from bfs import run_bfs


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding")

def main(win, width):
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
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_r:  # Reset
                    start = None
                    end = None
                    started = False
                    grid = make_grid(ROWS, width)
    pygame.quit()

def algorithm(draw, grid, start, end):
    # run_a_star(draw, grid, start, end)
    run_bfs(draw, grid, start, end)

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
main(WIN, WIDTH)