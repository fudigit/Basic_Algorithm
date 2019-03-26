'''
Loop each cell, when encounter island, flip all connected island to water
3 functions:
1. Loop through and count number of island
2. bfs: find connected island and flip to water
3. check if the next coordinat is inbound and an island


# put the 1st coordinates into deque: deque([(x,y)] 
'''


from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    
    # go through the grid, when hit island: count ++1, use bfs find and erase the entire island
        
    def numIslands(self, grid):
        num_islands = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(i,j)
                if grid[i][j] == True:
                    self.bfs_erase(grid,i,j)
                    num_islands += 1
        return num_islands
        
    
    # use bfs to find and erase the entire island(label all connected True to False)
    def bfs_erase(self, grid, x, y):
        grid[x][y] = False
        queue = deque([(x, y)])
        
        while queue:
            #print (queue)
            x, y = queue.popleft()

            for x_delta, y_delta in [(1,0),(0,-1),(-1,0),(0,1)]:
                x_next = x + x_delta
                y_next = y + y_delta
                if self.isValid(grid, x_next, y_next):
                    grid[x_next][y_next] = False
                    queue.append((x_next, y_next))
    
    # check if the (x,y) is in bound and an island
    def isValid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == True
