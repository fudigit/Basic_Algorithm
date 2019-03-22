'''
bfs, level order traveral + hashset for visted

1. n^2 matrix is a graph with n^2 nodes, for each node, it has 8 (maximum) neighbors
2. each level: 
    for each node in queue:
        check if the node reach destination
        then find its unvisited neighbors nodes, mark them as visisted and put them in queue

follow up, speed up
solution: double direction bfs

'''

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        
        moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        
        # find the distance, level order traversal
        queue = deque([source])
        visited = set([(source.x, source.y)])
        steps = 0
        
        while queue:
            print(queue)
            
            for _ in range(len(queue)):
                p = queue.popleft()
                
                if (p.x, p.y) == (destination.x, destination.y):
                    return steps
                
                for delta_x, delta_y in moves:
                    x_next = p.x + delta_x
                    y_next = p.y + delta_y
                    
                    if (x_next, y_next) in visited:
                        continue
                    
                    if self.is_valid(grid, x_next, y_next):
                        queue.append(Point(x_next, y_next))
                        visited.add((x_next, y_next))
                        
            steps += 1
        return -1
        
    # if the step is inbound and not on a barrier
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        if (0 <= x < n and 0 <= y < m) and grid[x][y] == False:
            return True
        
