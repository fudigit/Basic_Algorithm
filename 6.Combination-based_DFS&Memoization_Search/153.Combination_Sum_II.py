'''
# 1. skip the repeated number in the the same level ('for' loop).
# 2. adding repeated number into the next level is allowed!
'''

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum2(self, candidates, target):
        candidates = sorted(list((candidates)))
        results = []
        #self.level = 0      #check tree depth
        self.dfs(candidates, target, 0, [], results)
        return results
        
    def dfs(self, candidates, target, start, combination, results):
        #self.level += 1
        if target == 0:
            return results.append(list(combination)) # return, so no need to start another loop
            
        for i in range(start, len(candidates)):
            #print('i=', i, 'candi=',candidates[i], 'target=', target, 'start=', start, combination, 'level=', self.level)
            if candidates[i] == candidates[i-1] and i > start:
                continue
            
            if target < candidates[i]:
                return
            
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i+1, combination, results)
            combination.pop()
            #self.level -= 1
