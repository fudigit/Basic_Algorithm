'''
start from [], turn the combination into a binary tree problem
1. for each num in the list, decide weather add it(or not) into the subset:
2. the last level (leafs) is all the subsets
for [1,2]
[]
[1], [0]
[1,2],[1],[2],[0]
'''

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        results = []
        if nums == None:
            return results
        nums.sort()
        
        self.dfs(nums, 0, [], results)
        return results
        
    # 1. definition of recursion
    # 以 subset 开头的，配上nums以index开始的数的所有组合放到 results 里
    def dfs(self, nums, index, subset, results):
        
        # 3. exist of recursion: 已经得到方案
        if index == len(nums):
            results.append(subset[:])
            return
        
        # 2. devide and solve
        # pick nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, results)
        
        # does not pick nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset, results)
            
