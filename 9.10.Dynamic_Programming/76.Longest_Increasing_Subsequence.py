# 以每个点为起点，找最长，打擂台
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        
        # 以第i个数字为结尾的最长子序列的长度
        dp = [1 for i in range(length)]
        
        for cur in range(1, length):
            for prev in range(cur):
                if nums[prev] < nums[cur]:
                    dp[cur] = max(dp[prev] + 1, dp[cur])
        print(dp)
        return max(dp)
    
    
    class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        
        # 以第i个数字为结尾的最长上升子序列
        # 是否可以推导出以第i+1个数字为结尾的最长上升子序列？
        # 如果知道第1 ~ i的LIS, 求i+1？看第i+1个数字是否继续递增，取最长
        
        if not nums:
            return 0
            
        dp = [1 for i in range(len(nums))]
        
        for cur, val in enumerate(nums):
            tmp = 0
            for prev in range(cur):
                if val > nums[prev]:
                    tmp = max(tmp, dp[prev])
            tmp += 1
            dp[cur] = tmp
                    
        return max(dp)
