'''
use BFS
1. word latter can be considered as a graph, word being vertex, tranformation being ege
2. for each level, find the current words' neighbors, the unrepeated neighbors become the next level
3. finding the shortest sequence is equevalent to finding the level with the 'end' word

O(number of nodes) * O(L*25)
'''

from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        
        dict.add(end)
        queue = deque([start])
        visited = set([start])
        
        distance = 0
        
        while queue:
            # start word counts as 1
            distance += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                
                for next_word in self.get_next_word(word):
                    if next_word in dict and next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
        
        return 0
            
    
    
    # function to creat all possible next words, given current word
    # O(L*25), L = len(word)
    def get_next_word(self, word):
        char = 'abcdefghijklmnopqrstuvwxyz'
        next_words = []
        for i in range(len(word)):
            left, letter, right = word[:i], None, word[i+1:]
            for letter in char:
                if letter == word[i]:
                    continue
                next_w = left + letter + right
                next_words.append(next_w)
        
        return next_words
            
