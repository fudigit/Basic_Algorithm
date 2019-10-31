# 典型bfs，要注意分层遍历才能求出最短路径：遍历每一层，每个node下一步都有四种走法。
# 注意如何计算level数, 推荐每层遍历完以后加，下一层遍历的时候看入队的点是否已经是终点。
# 一开始特殊输入值要注意顺序，如果grid是空，那么起点，终点就不存在了
# is_valid 的顺序很重要，首先为in bound, 然后才能判断是否是barrier或者被visited
# O(m*n),因为矩阵大部分的点都需要被访问。可以想成是:每层所有的走法之和，就是全部被访问的点之和
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        if grid == [[]] or grid == []:
            return -1
        n, m = len(grid), len(grid[0]) 

        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        
        if n == 1 and m == 1:
            return 0
        # bfs by levle
        queue = collections.deque()
        queue.append((0,0))
        visited = set()
        
        level = 0
        delta_x = [1, -1, 2, -2]
        delta_y = [2, 2, 1, 1,]
        
        while queue:
            #level += 1, 再遍历开始时就加level，如果走到终点就 return level
            # for each node in the queue
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == (n - 1, m - 1):
                    return level
                # for each next step of the node
                for i in range(4):
                    x_next = x + delta_x[i]
                    y_next = y + delta_y[i]
                    if self.is_valid(x_next, y_next, n, m, grid, visited):
                        #if (x_next, y_next) == (n - 1, m - 1):
                        #    return level
                        visited.add((x_next, y_next))
                        queue.append((x_next, y_next))
            level += 1 #一层遍历完了，再加level。需要入queue的node做判断，是否是终点
        return -1
                    
    def is_valid(self, x_next, y_next, n, m, grid, visited):
        # out of bound
        if not (0 <= x_next < n and 0 <= y_next < m):
            return False
        # on barrier
        if grid[x_next][y_next] == 1:
            return False
        # visited
        if (x_next, y_next) in visited:
            return False
        return True
