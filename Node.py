import pygame
import color_constants

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row  # i value that is passed in from make_grid()
        self.col = col  # j value that is passed in from make_grid()
        self.x = row * width  # X Position of mouse in terms of 800 scren width (Halfway = 400)
        self.y = col * width  # Y Position of mouse in terms of 800 scren width (Halfway = 400)
        self.color = color_constants.WHITE    # All nodes originally start at white
        self.neighbors = []   # Will be filled in with top, bottom, left, and right neighbors
        self.width = width    # Gap between each node (16)
        self.total_rows = total_rows  # 50

    def get_coordinates(self):
        return self.row, self.col

    # Already checked
    def is_closed(self):
        return self.color == color_constants.RED

    # Going to check next
    def is_open(self):
        return self.color == color_constants.GREEN
    
    def is_barrier(self):
        return self.color == color_constants.BLACK
    
    def is_start(self):
        return self.color == color_constants.ORANGE

    def is_end(self):
        return self.color == color_constants.TURQUOISE
    
    def reset(self):
        self.color = color_constants.WHITE

    def make_start(self):
        self.color = color_constants.ORANGE
    
    def make_closed(self):
        self.color = color_constants.RED
    
    def make_open(self):
        self.color = color_constants.GREEN
    
    def make_barrier(self):
        self.color = color_constants.BLACK

    def make_end(self):
        self.color = color_constants.TURQUOISE

    def make_path(self):
        self.color = color_constants.PURPLE
    
    def draw(self, win):
        # Draws the rectangle at         winPosX, winPosY with height and width of gap (16)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
   
    # Checks if up/down/left/right are barriers
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # Down neighbor
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # Up neighbor
            self.neighbors.append(grid[self.row - 1][self.col])
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # Right neighbor
            self.neighbors.append(grid[self.row][self.col + 1])
        
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # Left neighbor
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
