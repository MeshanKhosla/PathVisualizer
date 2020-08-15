from dfs import reconstruct_path
import pygame

def run_bfs(draw, grid, start, end, reconstruct_path):
    queue = [start]
    checked = {start}
    parent = {start: None}
    # current_node = None

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        next = []
        for node in queue:
            # current_node = node
            
            if node == end:
                reconstruct_path(parent, end, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in node.neighbors:
                if neighbor not in checked:
                    neighbor.make_closed()
                    checked.add(neighbor)
                    parent[neighbor] = node
                    next.append(neighbor)
                    
            if node != start:
                node.make_open()
        queue = next

        draw()
        