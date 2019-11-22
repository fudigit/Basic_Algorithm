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
