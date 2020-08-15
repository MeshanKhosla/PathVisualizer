import pygame


def run_dfs(draw, grid, start, end, reconstruct_path):
    parent = {start: None}
    queue = [start]
    visited = set()

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        current_node = queue.pop()
        visited.add(current_node)
        current_node.make_cur_node()

        if current_node == end:
            end.make_end()
            start.make_start()
            reconstruct_path(parent, end, draw)
            end.make_end()
            start.make_start()
            return True


        for neighbor in current_node.neighbors:
            neighbor.make_closed()
            if neighbor not in visited:
                neighbor.make_open()
                parent[neighbor] = current_node
                queue.append(neighbor)
                
        end.make_end()
        start.make_start()
        draw()
    return False





