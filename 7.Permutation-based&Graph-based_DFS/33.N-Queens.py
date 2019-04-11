'''
permutation
trick: a permutation of the numbers can represent the queen on the drawChessboard
i.e., [1,3,0,2] -> (0,1), (2,3), (3,0), (4,2) has a queen

# 1. The question become finding a permutation such that no queen can attack other queens
# 2. Use a drawChessboard function to draw the chessBoard
# 3. Use a isValid function make sure the queen on next row cannot attack any previous qeen
'''

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        results = []
        if n == 0 or n is None:
            return results
        self.dfs_permut(n, [], results)
        return results
            
    # find all distinct solutions starts with cols (position of Q in each row)
    def dfs_permut(self, n, cols, results):
        # row
        row = len(cols)
        if len(cols) == n:
            results.append(self.drawChessboard(cols))
            return
        
        for i in range(n):
            col = i
            if not self.isValid(cols, row, col):
                continue
            cols.append(col)
            self.dfs_permut(n, cols, results)
            cols.pop()
                
    
    # give position of Q in each row, drawChessboard
    def drawChessboard(self, cols):
        row_len = len(cols)
        board = []
        for i in range(row_len):
            row = ['Q' if j == cols[i] else '.' for j in range(len(cols))]
            board.append(''.join(row))
        return board
        
        
    # check if the current cell can be attached by the existing queens
    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if col == c:
                return False
            # Diagnal attack: r-c = row-col, i.e.(1 - 1 = 3 - 3), r + c = row + col, i.e.(1 + 2 = 2 + 1 = 3 + 0)
            if r - c == row - col or r + c == row + col:
                return False
        return True
        
