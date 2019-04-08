'''
1. use range(1, n + 1) as the list of candidates
2. find the subset (without reapeating) using dfs
3. constraint: return when there are k elements 

'''

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        results = []
        if n is None or k is None:
            return results
        
        self.dfs(n, k, 1, [], results)
        return results
        
    # when combination has k elements, add all combinations start with 'start' to results
    def dfs(self, n, k, start, combination, results):
        # deep copy
        if k == 0:
            results.append(list(combination))
            return
        
        for i in range(start, n + 1, 1):
            combination.append(i)
            self.dfs(n, k - 1, i + 1, combination, results)
            combination.pop()
            

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
