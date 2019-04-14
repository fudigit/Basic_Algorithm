'''
BFS + DFS on graph
1. BFS from end to start, count each node's distance to end, saving a distance hashmap
2. DFS from start to end, ensure every step make the distance to end closer!
3. finding next_words: every ward has L char, each char has 25 changes, new word shall in dict

errors
1. how to import deque
2. wrong identation when defining the function
3. deep copy in dfs

logic
1. in bfs, if next_word is already in distance hashmap, skip it, since it's going back in graph
    - direction of deque for FIFO? Both work: Left in right out; right in left out
    - use distance hashmap = {}: 1. avoid go back in graph, 2. track the steps to target
        - in Word Latter 1, used visted = set() to avoid go back in the graph
    - not level order traversal required
2. in dfs, would the distance[next_word] != distance[start] - 1 garantee there is no turning back in graph?
3. what's the purpose of dfs?

review
why not use BFS directly? - try use it directly, shall work, but slow
- will get into the paths that won't lead to the shortest path, in bfs, each node is a paths
- get the distance to the end with BFS, helps avoid picking longer path in DFS (2 BFS should also work)
- BFS 在树上，在图上还是不熟， 什么时候可以不用level order traversal，deque怎么使用，怎么根据当前层找出下一层，避免往回走
- DFS 在图上，需要哪些参数?(cur, end), dict, distance, (path, result)如何避免往回走？什么时候需要deepcopy？
'''
from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
    # main
        dict.add(start) # may start from the end
        dict.add(end)
        distance = self.bfs_getDistance(end, start, dict)
        #print(distance)
        
        results = []
        path = [start]
        self.dfs_findPath(start, end, dict, distance, path, results)
        
        return results
    
    # do a bfs from target to start, get the distance from node to the target
    def bfs_getDistance(self, start, end, dict):
        distance = {}
        queue = deque([start])
        distance[start] = 0
        while queue:
            for _ in range(len(queue)): # can work without level order traversal
                word = queue.popleft()
                next_words = self.find_nextWords(word, dict)
                for next_word in next_words: 
                    if next_word not in distance: # if _next_word already in distance, it's visited
                        distance[next_word] = distance[word] + 1
                        queue.append(next_word)
        return distance
    
    # get the next word
    def find_nextWords(self, word, dict):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        next_words = []
        for i in range(len(word)):
            for char in alphabet:
                next_word = word[:i] + char + word[i+1:] #replace ith letter with char
                if next_word != word and next_word in dict: #only prevent getting the same word
                    next_words.append(next_word)
        return next_words
                

    # dfs with contraint to always reduce distance to the target 
    # find the shortest path to target from the current word: curt, append the path to results
    def dfs_findPath(self, curt, end, dict, distance, path, results):
        if curt == end:
            results.append(list(path))  # deep copy!
            return
        
        next_words = self.find_nextWords(curt, dict)
        for next_word in next_words:
            if distance[next_word] != distance[curt] - 1:  # will this guarantee no turning back?
                continue
            path.append(next_word)
            #print(next_word, path)
            self.dfs_findPath(next_word, end, dict, distance, path, results)
            path.pop()
            
