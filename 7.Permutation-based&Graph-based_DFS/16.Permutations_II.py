'''
purmutations with duplicate numbers
use dfs with dup tweak

How to avoid dups?
i.e, [1,2,2']
[1,2,2'] and [1,2',2] will be dups, what are their paths?
1. [1] -> [1,2] -> [1,2,2']
2. [1] -> [1,2'] -> [1,2',2]
# - we only pick path 1, so in the for loop, if previous # is the same and has not been visited, skip
# - note the number need to be sorted, so the same nums are together

# if nums = [1,1,1,1,1,1], O(n^2): n level, n traversal in each level
# in general, O(S * n^2), S is # of solutions, it take n^2 time to find one path
'''


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permuteUnique(self, nums):
        results = []
        if nums is None:
            return results
        # nums = [], resultswill out put [[]]
        
        nums.sort()
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
            
            # repeating number with the previous number not bieng visited, dup will be created
            if i > 0 and nums[i] == nums[i-1] and visited[i-1] is False:
                continue
            
            permutation.append(nums[i])
            visited[i] = True
            #print(nums[i], permutation)
            self.dfs_permute(nums, visited, permutation, results)
            visited[i] = False
            permutation.pop()
                
