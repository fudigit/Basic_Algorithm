'''V1
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
        
        
'''V2
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
            

'''V3
Brute force，慢得跑不出结果
O(n^2)
'''
class Solution:
    def maxSubArray(self, nums):
        
        max_sub = -sys.maxsize
        
        # fix left end of the subarray
        for i in range(len(nums)):
            r = i
            i_start_sub = 0
            
            # move the right end of the subarray
            while r <= len(nums) - 1:
                i_start_sub += nums[r]
                if i_start_sub > max_sub:
                    max_sub = i_start_sub
                r += 1
        
        return max_sub
            
'''V4 dp
https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
'''
# define a sub probelm, that if it is solved, it helps solve the next-step sub problem
# sub problem: local_max(i) is the maximum subarray that ends with nums[i]
# local_max(i + 1) = max(local_max(i) + nums[i + 1], nums[i + 1])
# note, local_max(i + 1) = (local_max(i) > 0)? local_max(i) + nums[i + 1] VS nums[i + 1]

class Solution:
    def maxSubArray(self, nums):
        global_max = -sys.maxsize
        local_max = -sys.maxsize
        
        for n in nums:
            local_max = max(local_max + n, n)
            global_max = max(global_max, local_max)
        
        return global_max

    
# 由左向右遍历，每加入一个新元素前，看之前的array sum是否>0, 换言之是否带来增益。
# 如果<0，则没有增益，一定不属于max subarray。和V4方法类似

class Solution:
    def maxSubArray(self, nums):
        if nums == [] or nums is None:
            return 0
        
        global_max = -sys.maxsize
        pos_sum = 0
        
        for n in nums:
            pos_sum = pos_sum + n
            global_max = max(global_max, pos_sum)
            pos_sum = max(pos_sum, 0)
        
        return global_max
