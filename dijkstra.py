import pygame
from queue import PriorityQueue


def run_dijkstra(draw, grid, start, end, reconstruct_path):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    parent = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    open_set_hash = {start}  # Priority queue is not iterable

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current_node = open_set.get()[2]  # 3rd parameter in open_set value is the actual node
        open_set_hash.remove(current_node)

        if current_node == end:
            reconstruct_path(parent, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current_node.neighbors:
            temp_g_score = g_score[current_node] + 1  # The weight for every node traversal is 1

            if temp_g_score < g_score[neighbor]:
                parent[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((g_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current_node != start:
            current_node.make_closed()
    return False  # Did not find path
