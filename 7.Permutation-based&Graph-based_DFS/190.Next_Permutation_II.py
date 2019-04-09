'''
- traverse array from right to left, the first non-increasing integer X must be pulled into the right side,
- its position will be replaced by the smallest number greater than X on X's right side
- after replacement, the number on the right side need to be increasing
'''

class Solution:
    
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        
        if len(nums) <= 1:
            return
        
        i = len(nums) - 1
        
        while i > 0 and nums[i - 1] >= nums[i]:  # >=
            i -= 1

        if i != 0:
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:  # note nums[i:] is monotone decrease, # strictly greater than nums[i-1]
                j -= 1
            
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        #print(nums, nums[i:])
        #contain case if i == 0
        self.swap(nums, i, len(nums) - 1)
        return nums
        
        
    def swap(self, sub_nums, i, j):
        while i < j:
            sub_nums[i], sub_nums[j] = sub_nums[j], sub_nums[i]
            i += 1
            j -= 1
        #return sub_nums, don't return!
        
        
