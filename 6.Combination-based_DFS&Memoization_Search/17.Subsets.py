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
        
        
'''
# 排列搜索类递归
# use dfs to find all subsets based on a fixed head-subset
[]

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
        
    # defintion of recursion
    # 寻找以subset开头，与nums[index]及之后数字形成的所有子集，加入到results
    def dfs(self, nums, startIndex, subset, results):
        # each subset is a valid combination
        # subset 的地址被传到下一层，所以要深考
        results.append(subset[:])
        
        for i in range(startIndex, len(nums), 1):
            # [1] => [1,2]
            # 去寻找以 [1,2] 开头的所有子集
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            # [1,2] => [1], 下一个dfs状态和这次相同：[1] => [1,3]
            subset.pop() #backtracking
            
        
            
