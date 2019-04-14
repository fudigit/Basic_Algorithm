'''
error:
1. Capitalize contstant!
2. convert result to list
3. not in visited or in visited
4. not in board or in board
4. string has not pop
'''

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        self.next_move = [(1,0), (0,-1), (-1,0), (0,1)] 
        results = set()
        
        # 
        # construct a set of prefix, as well as the word itself, can be used in search
        words_dict = set(words) # make the search time O(1)
        prefix_dict = set()
        for word in words_dict:
            for i in range(len(word)):
                prefix_dict.add(word[:i + 1])

        # start from each position of the matrix, use dfs to find the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                print(char)
                self.dfs_findPath(board, i, j, char, words_dict, prefix_dict, set(), results)
                
        return list(results) # convert since results is a set!
        
        
        # use dfs to find path of word
    def dfs_findPath(self, board, x, y, word, words_dict, prefix_dict, visited, results):
        if word in words_dict:
            results.add(word)
            return
        if word not in prefix_dict:
            return
            
        for x_move, y_move in self.next_move:
            x_, y_ = x + x_move, y + y_move
                
            if (x_, y_) in visited:
                continue
            if not self.isInBoard(board, x_, y_):
                continue
                
            visited.add((x_, y_))
            #word_added = word + board[x_][y_]
            print(board[x_][y_],x_, y_,'hey', visited)
            self.dfs_findPath(board, x, y, word + board[x_][y_], words_dict, prefix_dict, visited, results)
            #word_added.pop()
            visited.remove((x_, y_))
                
        # make sure x, y is in boundary 
    def isInBoard(self, board, x, y):
        n, m = len(board), len(board[0])
        if 0 <= x < n and 0 <= y < m:
            return True
        return False
            
