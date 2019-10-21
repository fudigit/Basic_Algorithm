'''
use prefix + hashmap
1. record the prefix_sum and its index that has first encountered
2. if a second encounter for the same prefix_sum, interval of sum 0 has found!

prefix_sum[i] = A[0] + A[1] + .. + A[i]
sum(i, j) = 0 = prefix[j] - prefix[i-1]
=> prefix[j] = prefix[i-1]
sum(i, j) means finding 2 prefix_sum has equal value

使得prefix_sum包含A[i],会让思考简单一些

TC: O(n)
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        
        prefix_sum = 0
        prefixToIndex = {0:-1}
        
        for i in range(len(nums)):
            prefix_sum = prefix_sum + nums[i] # prefix is nums[0] + nums[1] + ... + nums[j]
            # print(j,prefixToIndex, prefix)
            if prefix_sum not in prefixToIndex:
                prefixToIndex[prefix_sum] = i
            elif prefix_sum in prefixToIndex:
                return prefixToIndex[prefix_sum] + 1, i

        return -1, -1


    
'''    
2 刷
# 坐标为i至j的数的和, sum(i~j) = 0  ==>  prefix(j+1) - prefix(i) = 0 
# prefix(j+1) = prefix(i)
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        prefix_dict = {}
        prefix_dict[0] = 0
        
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix not in prefix_dict:
                prefix_dict[prefix] = i + 1
            elif prefix in prefix_dict:
                print(prefix_dict)
                return [prefix_dict[prefix], i + 1 - 1]
            
            
'''
3刷，定义prefix(j) = A[0] + ... + A[j]。注：与九章定义不同，九章为前j个数，这里是前j + 1个数。这个定义更直观
# 坐标为i至j的数的和, sum(i~j) = 0  ==>  prefix(j) - prefix(i-1) = 0 ，注意，保留A[i]!
# 反之，如果prefix(j) - prefix(k) = 0, 说明sum(k+1, j) = 0
# 建立一个value to index的mapping，从左往右边记录prefix_sum，去找j和k，such that prefix(j) - prefix(k) = 0
# - 说明sum(k+1, j) = 0
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        valueToIndex = {}
        valueToIndex[0] = -1 #prefix(-1) = 0, A[-1] = None
        
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum not in valueToIndex:
                valueToIndex[prefix_sum] = i
            elif prefix_sum in valueToIndex:
                # the ask is the index of the 1st and last num in sub, not to print the subarray
                return [valueToIndex[prefix_sum] + 1, i]
                
        return 'no subarray found'
