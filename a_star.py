import pygame
from queue import PriorityQueue

# Gets manhattan distance (L shape)
def h(p1, p2):
    x1, y1 = p1   #p1 will be like (1, 2), so x1 = 1 and y1 = 2
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def run_a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_coordinates(), end.get_coordinates())  # Sets f score of start node to the manhattan distance (h(n))

    open_set_hash = {start}  # Priority queue is not iterable

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current_node = open_set.get()[2]  # 3rd parameter in open_set value is the actual node
        open_set_hash.remove(current_node)

        if current_node == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current_node.neighbors:
            temp_g_score = g_score[current_node] + 1  # The weight for every node traversal is 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_coordinates(), end.get_coordinates())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current_node != start:
            current_node.make_closed()
    return False  # Did not find path

    
def reconstruct_path(came_from, current, draw):
    while current in came_from:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                
        current = came_from[current]   # Goes backwards until start node
        if current: current.make_path()
        draw()