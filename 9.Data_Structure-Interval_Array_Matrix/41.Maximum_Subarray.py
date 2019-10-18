'''
1,2,3,6,8,9,0,-5,6
|   |     | |
0   i     j j+1

1. create a prefix sum, such that the interval sum is the difference between 2 prefix sum:
def: prefix[i] = A[0] + A[1] + A[2] + ... + A[i-1], prefix[0] = 0
sum(i to j) = prefix[j+1] - prefix[i] = A[i] + A[i+1] + ... + A[j]

getting the max_sum: prefix[j] - min(prefix{0~j-1})

O(n)
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums == [] or nums == None:
            return 0
        
        max_sub = nums[0]
        prefix_sum = 0
        min_prefix_prior = 0
        
        for i in range(len(nums)):
            #print(prefix_sum, max_sub, min_prefix_prior)
            prefix_sum = prefix_sum + nums[i]
            max_sub = max(max_sub, prefix_sum - min_prefix_prior)
            min_prefix_prior = min(min_prefix_prior, prefix_sum)
        return max_sub
        
        
'''
2刷，拿到题目没印象了

# 构造一个 prefix sum
# prefix sum is defined as prefix[i] = nums[0] + ..., nums[i-1], where prefix[0] = 0
# then we can write Sum(i ~ j) as prefix[j+1] - prefix[i]
# 前j+1个数之和，减去前i个数之和，就是下标为i到下标为j的数之和。

# 使用前缀和的方法，计算每个位置为结尾的subarray的最大值
# 前缀和减去前缀和最小，得到subarray最大。
'''
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        
        if nums is None or nums is []:
            return 0
            
        prefix_sum = 0
        # 记录前缀和
        max_sum = - sys.maxsize
        # 记录全局最大
        prefix_min_sum = 0
        # 记录前i个数中(nums[:i])的最小前缀和sum(0 ~ k), where k <= i
        
        #注意前缀和最小是后更新的，否则会重合
        for num in nums:
            prefix_sum = prefix_sum + num
            max_sum = max(prefix_sum - prefix_min_sum, max_sum)
            prefix_min_sum = min(prefix_min_sum, prefix_sum)

        return max_sum
            
        
