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
            
# 2 刷 决策树法
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        result = []
        if nums == None:
            return result
        
        nums = sorted(nums)
        self.dfs(nums, 0, [], result)
        
        return result
        
        
    # definition: for each integer from left to right, decide if to include in the subset or not 
    def dfs(self, nums, index, sub, result):
        
        if index == len(nums):
            result.append(sub[:])
            return
            
        # left, to not include
        self.dfs(nums, index + 1, sub, result)

        
        # right, to include
        sub.append(nums[index])
        self.dfs(nums, index + 1, sub, result)
        sub.pop()  #注意这里回溯的重要性，否则sub会保持append到result时候的状态。


## 2刷，可拓展到排列搜索的递归模板
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        result = []
        if nums == None:
            return result
        
        nums.sort()
        self.dfs(nums, 0, [], result)
        
        return result
    
    def dfs(self, nums, start, subset, result):
        
        result.append(subset[:])
        # no need for return, taken cared by for
'''# 内部调用dfs，起始位置必须是i+1,如此保证枚举每个路径唯一
     原则是，找到以i为开头的所有路径，subset可以理解成找到包含了A的所有子集'''    
        for i in range(start, len(nums)):
            
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, result)
            subset.pop()

# 不加入index作为参数，而用判断语句确保加入新的元素
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        result = []
        if nums == None:
            return result
        nums = sorted(nums)
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, subset, result):
        result.append(subset[:])
        for i in range(len(nums)):
            if len(subset) == 0 or len(subset) > 0 and subset[-1] < nums[i]:
                subset.append(nums[i])
                self.dfs(nums, subset, result)
                subset.pop()
            
#bfs
from collections import deque

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    # bfs
    def subsets(self, nums):
        result = []
        if nums == None:
            return result
        
        nums = sorted(nums)
        self.bfs(nums, result)
        return result
        
    def bfs(self, nums, result):
        queue = deque([])
        queue.append([]) #注意1.deque是如何定义的。 2.这道题，deque里装的是lists，而非单个元素
        while queue:
            subset = queue.popleft()[:]
            result.append(subset)
            for i in range(len(nums)):
                if subset == [] or subset[-1] < nums[i]:
                    new_sub = subset[:]
                    new_sub.append(nums[i])
                    queue.append(new_sub)
                    
from collections import deque



# bitwise operation
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    # bfs
    def subsets(self, nums):
        result = []
        if nums == None:
            return result
        
        nums = sorted(nums)
        n = len(nums)
        
        for i in range(1 << n):
            subset = []
            for j in range(n):
                print(i&1, j)
                if i & 1 << j != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
      
      
