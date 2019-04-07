'''
recursion
some iterations from 17.Subsuets will add duplicates, how to avoid?
1. within each recursion (same tree level), appending the same element (2nd time) shall be avoided
2. for a new recursion(another tree level), always add the first element, no matter dup or not.

Method 2:
如果前面相同的数没有选，后面的数就不能选。 [1,1,1] 如果第一个1没有选，那么for循环中就不能选第二个1, i != startindex，说明跳数
'''

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        results = []
        if nums is None:
            return results
        
        nums.sort()
        self.counter = 0
        self.dfs(nums, 0, [], results)
        return results
        
    # 找到所有以subset开始的子集，加入到result
    def dfs(self, nums, startIndex, subset, results):
        results.append(subset[:])
        
        for i in range(startIndex, len(nums), 1):
            self.counter += 1
            print(self.counter)
            # i > startIndex: so that nums[startIndex] (first of next recursion) is added
            # since start of next recursion is adding additional elements: [2].append(2)
            if i != 0 and nums[i] == nums[i-1] and i > startIndex:
                continue
            
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()
