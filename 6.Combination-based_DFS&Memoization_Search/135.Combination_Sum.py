
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))    # set is use to rid of unique
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

            if target < candidates[i]:
                return
            
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()
            #self.level -= 1

### 2 刷
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candi = list(set(candidates))
        candi = sorted(candi)
        
        result = []
        count = 0
        self.dfs_helper(candi, 0, target, [], result, count)
        return result
        
        
    def dfs_helper(self, candidates, start, target, combination, result, count):
        count += 1
        print(combination, count)
        if target < 0:
            return
        
        if target == 0:
            return result.append(combination[:])
        
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs_helper(candidates, i , target - candidates[i], combination, result, count)
            combination.pop()
            
