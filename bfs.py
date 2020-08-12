import pygame

def run_bfs(draw, grid, start, end):
    queue = [start]
    checked = {start}
    came_from = {start: None}
    # current_node = None

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        next = []
        for node in queue:
            # current_node = node
            
            if node == end:
                reconstruct_path(came_from, end, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in node.neighbors:
                if neighbor not in checked:
                    neighbor.make_closed()
                    checked.add(neighbor)
                    came_from[neighbor] = node
                    next.append(neighbor)
                    
            if node != start:
                node.make_open()
        queue = next

        draw()
        
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        current = came_from[current]   # Goes backwards until start node
        if current: current.make_path()
        draw()