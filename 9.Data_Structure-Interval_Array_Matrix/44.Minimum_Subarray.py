'''
use prefix
similar to 41.Maximum_Subarray.py
def: prefix[i] = A[0] + A[1] + A[2] + ... + A[i-1], prefix[0] = 0
sum(i to j) = prefix[j+1] - prefix[i] = A[i] + A[i+1] + ... + A[j]

minimum_sum of A[0 to j-1] = prefix(j) - max(prefix{1 ~ j-1})
'''

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        if nums == [] or nums == None:
            return 0
            
        prefix_sum = 0
        min_sum = nums[0]
        max_prefix_prior = 0
        
        for i in nums:
            prefix_sum = prefix_sum + i
            min_sum = min(min_sum, prefix_sum - max_prefix_prior)
            max_prefix_prior = max(max_prefix_prior, prefix_sum)
            
        return min_sum
        
        
