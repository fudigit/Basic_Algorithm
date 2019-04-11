
'''
permutation
trick: a permutation of the numbers can represent the queen on the drawChessboard
i.e., [1,3,0,2] -> (0,1), (2,3), (3,0), (4,2) has a queen

# 1. The question become finding a permutation such that no queen can attack other queens
# 2. Use a drawChessboard function to draw the chessBoard
# 3. Use a isValid function make sure the queen on next row cannot attack any previous qeen

# how to solve with _usedColumns
'''

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        self.count = 0
        if n == 0 or n is None:
            return self.count
        self.dfs_permut(n, [])
        return self.count
            
    # find all distinct solutions starts with cols (position of Q in each row)
    def dfs_placeQueen(self, n, cols):
        # row
        row = len(cols)
        if len(cols) == n:
            self.count += 1
            return
        
        for i in range(n):
            col = i
            if not self.isValid(cols, row, col):
                continue
            cols.append(col)
            self.dfs_placeQueen(n, cols)
            cols.pop()
        
    # check if the current cell can be attached by the existing queens
    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if col == c:
                return False
            # Diagnal attack: r-c = row-col, i.e.(1 - 1 = 3 - 3), r + c = row + col, i.e.(1 + 2 = 2 + 1 = 3 + 0)
            if r - c == row - col or r + c == row + col:
                return False
        return True
        
