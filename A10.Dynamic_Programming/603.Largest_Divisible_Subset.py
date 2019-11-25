class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        if not nums: return nums
        
        # dp[i]是以nums[i]为最大元素的最大可除子集(LDS)里元素的个数
        dp = [1]*len(nums)
        # father 记录当前nums[i]为最大元素对应的上一个最大元素的index。
        # i.e., 记录dp[i]+1是选择了哪一个之前的dp[prev]；最优值是由哪个prev算过来的
        father = [-1]*len(nums)
        # 必须递增，才能由小推大
        nums.sort()
        # 记录最大可除子集里元素的个数，和值最大元素的index
        max_length, index = 0, -1
        
        for cur in range(1, len(nums)):
            for prev in range(cur):
                if nums[cur] % nums[prev] == 0:
                    if dp[prev] + 1 > dp[cur]:
                        dp[cur] = dp[prev] + 1
                        father[cur] = prev
            # 打擂台，找LDS的个数，和最大元的index
            if dp[cur] > max_length:
                max_length = dp[cur]
                index = cur
                
        
        LDS = []
        # 知道个数，需要要max_length - 1次
        for _ in range(max_length):
            LDS.append(nums[index])
            index = father[index]
            
        return LDS
            
                        
