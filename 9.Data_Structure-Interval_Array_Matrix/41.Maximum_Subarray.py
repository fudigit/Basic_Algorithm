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
        
        
        
