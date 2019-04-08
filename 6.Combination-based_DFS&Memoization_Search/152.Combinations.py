'''
1. use range(1, n + 1) as the list of candidates
2. find the subset (without reapeating) using dfs
3. constraint: return when there are k elements 

O(c(n,k)*k)
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
            



'''
1. create the list of [1, ..., n]
2. find the subset (without reapeating) using dfs
3. constraint: return when there are k elements 
slow, O(C(n,k)*k)
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
        
        candidates = [i for i in range(1, n + 1, 1)]
        self.dfs(candidates, k, 0, [], results)
        return results
        
    # when combination has k elements, add all combinations start with 'start' to results
    def dfs(self, candidates, k, start, combination, results):
        if k == 0:
            results.append(list(combination))
            return
        
        for i in range(start, len(candidates), 1):
            
            combination.append(candidates[i])
            self.dfs(candidates, k - 1, i + 1, combination, results)
            combination.pop()
            
