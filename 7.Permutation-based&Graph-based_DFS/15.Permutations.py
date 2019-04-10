'''
purmutations
use dfs
1. use a boolean list 'visited' to track the integers that has been visited
2. in each level, pick a number from right to left, do not pick the number that has already be picked
'''


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        results = []
        if nums is None:
            return results
        # nums = [], resultswill out put [[]]
        
        visited = [False for i in range(len(nums))]
        self.dfs_permute(nums, visited, [], results)
        return results


    # find all permuation starts with certain permutation
    def dfs_permute(self, nums, visited, permutation, results):
        
        #exit
        n = len(nums)
        if len(permutation) == n:
            results.append(list(permutation))
            return
            
            
        for i in range(0, n):
            if visited[i]:
                continue
            
            permutation.append(nums[i])
            visited[i] = True
            #print(nums[i], permutation)
            self.dfs_permute(nums, visited, permutation, results)
            visited[i] = False
            permutation.pop()
