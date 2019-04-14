'''
use dfs + hash table
# 1. construct a prefix dict to check if the itermediate search result is on the right path
# 2. do search for every char in the board
# 3. if the path starts with the char exists in prefix, continue search in all directions
In gnenral, search problem has time complexity of NP time: 2^n, n!, C(n,m). Polinolial time: n^K
'''

'''
errors:
1. Capitalize contstant!
2. convert result (set()) to list
3. not in visited or in visited? If in, skip, because on char can be used once 
4. not in board or in board
5. string has not pop
6, visited starts with {(i, j)}, the position of the initial char
7. when added a word to result, return not required, since longer word may exists
8, do next dfs on x_, y_, not x, y!
'''
DIRECTIONS = [(1,0), (0,-1), (-1,0), (0,1)] # definine as constant outside of class
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        
        # construct a set of prefix, including the word itself, if path not in prefix, break
        words_dict = set(words) # make the search time O(1)
        prefix_dict = set()
        for word in words_dict:
            for i in range(len(word)):
                prefix_dict.add(word[:i + 1])

        # start from each position of the matrix, use dfs to find the word
        results = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                self.dfs_findPath(board, i, j, char, words_dict, prefix_dict, set([(i,j)]), results)
                
        return list(results) # convert since results is a set!
        
        
        # find path starting from word with path in the dict, add the path found into the results
    def dfs_findPath(self, board, x, y, word, words_dict, prefix_dict, visited, results):
        # exist
        if word in words_dict:
            results.add(word)      #longer word may exist, do not return
        
        if word not in prefix_dict:
            return
        
        # increase the path by 1 step on each possible directions
        for x_move, y_move in DIRECTIONS:
            x_, y_ = x + x_move, y + y_move
            
            # check if the next position is not visied, and in board
            if (x_, y_) in visited:
                continue
            if not self.isInBoard(board, x_, y_):
                continue
                
            visited.add((x_, y_))
            #word_added = word + board[x_][y_]
            #print(board[x_][y_],x_, y_,'sub dfs', visited, word + board[x_][y_])
            self.dfs_findPath(board, x_, y_, word + board[x_][y_], words_dict, prefix_dict, visited, results)
            #word_added.pop()
            visited.remove((x_, y_))
                
        # make sure x, y is in bound 
    def isInBoard(self, board, x, y):
        n, m = len(board), len(board[0])
        if 0 <= x < n and 0 <= y < m:
            return True
        return False
            
