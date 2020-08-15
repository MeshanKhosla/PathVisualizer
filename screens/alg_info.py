info = {

    "A*": {
            1:  "The A* (pronounced 'A star') pathfinding algorithm is very similar to Dijkstra's. I'd suggest you",
            2:  "read the information about Dijkstra's if you haven't read it yet. A* introduces one more",
            3:  "component to Dijkstra's, known as the H score. The H score is short for heuristic, and it ",
            4:  "finds an estimate of the distance from the current node until the end node. In the",
            5:  "visualization, I used Manhattan distance, which finds an 'L' shape route to the path.",
            6:  "Therefore, A* is often seen as a more efficient version of Dijkstra's since it is informed,",
            7:  "meaning it is not simply trying all possibilities until it gets to the end. In the visualization,",
            8:  "you'll see that the computer knows in what general direction to go in, whereas Dijkstra's goes",
            9:  "in every direction where there isn't a barrier. The computation for the algorithm is" ,
            10: "F(n) = G(n) + H(n). The G score -- G(N) -- is the distance from the start node to the current",
            11: " node. Adding the G score to the heuristic value gives us an F score, and we take the smallest F",
            12: "score every iteration in order to find the shortest path.", 
          },

    "Breadth First Search": {
        1: "Breadth First Search (or BFS) is a shortest path finding algorithm that focuses on queues.",
        2: "Every neighbor that is not a barrier is placed into a queue, and then every neighbor of that",
        3: "neighbor is places into a queue, and so on. It is called breadth first search because it",
        4: "traverses the graph layer by layer. Unlike its' depth first search counterpart, BFS looks like",
        5: "it is expanding from the start node. BFS is a First In, First Out (FIFO) algorithm, meaning the",
        6: "next node in the queue will be checked regardless of efficiency. When the ending node is found,",
        7: "BFS has kept track of which node every node came from, so it can now follow the path back to",
        8: "the start, resulting in the shortest path.",
    },

    "Dijkstra": {
        1: "Dijkstra's algorithm is one of the most popular shortest path finding algorithms. Dijkstra's",
        2: "is not informed, meaning it will not know which direction to start the search from. Therefore,",
        3: "Dijkstra's looks similar to BFS since they both go in all directions where there is no barrier.",
        4: "However, Dijkstra's is not a FIFO algorithm, meaning it does not simple check the nodes in the",
        5: "orders they were placed into the queue. Instead, Dijkstra's uses a priority queue to get the",
        6: "current shortest path from the starting node to the current node. It then uses this node to",
        7: "find its' next node. Other informed search algorithms, such as A* are based on Dijkstra's. Upon",
        8: "finding the end node, Dijkstra's traverses the path it's made backwards to find the shortest path.",
    },

    "Depth First Search": {
        1: "Depth First Search (or DFS) is not a shortest path finding algorithm. This is why the",
        2: "visualization looks very inefficient, but I think it's an interesting comparison to BFS.",
        3: "In DFS, one neighbor is taken from the starting node, and that neighbor is explored further.",
        4: "This process continues with every visited neighbor. Since only one node is visited at a time,",
        5: "the visualization looks snake-like, where the snake is inefficiently traversing the entire node",
        6: "looking for the end node.  When the snake finds the end node, it traverses its' path, which",
        7: "often takes a long time."
    },

}
