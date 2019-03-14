'''
use 2 pointers and number k to partition the array
1. find >= k using left pointer, and find < k using the right pointer, swap the 2 pointers
2. the set up of left and right pointer makes sure that: left side of left pointer <k, right side of right pointer >= k
3. use l =< r for the while condition: so l is always on the first element of >= k
    i.e., l = i, r = i + 1 => l = i + 1, r = i
          l = r = i => l = i + 1, r = i -1
4. if use l < r the while condition, l can either be on last of < k, or first of >= k
'''


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if nums == []:
            return 0
        
        l, r = 0, len(nums)-1
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] >= k:
                r -= 1
            if l <= r:
                print(nums, l, r)
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            print(l,r)
        
        #if l == len(nums)-1:
        #    return len(nums)
        return l
            
            
        
        
        
