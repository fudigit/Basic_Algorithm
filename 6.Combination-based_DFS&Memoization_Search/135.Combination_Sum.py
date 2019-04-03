class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        
        self.dfs(candidates, target, 0, [], results)
        return results
        
    def dfs(self, candidates, target, start, combination, results):
        if target == 0:
            results.append(list(combination))
            
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()
