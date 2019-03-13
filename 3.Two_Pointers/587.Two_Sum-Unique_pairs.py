'''
sort array + 2 same direction pointers
1. sort array in asending order
2. once a pair is found, let both pointer skip the same number used in the pair
3. search continue with different numbers
'''

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        
        nums.sort()
        
        l, r = 0, len(nums)-1
        count = 0
        
        while l < r:
            if nums[l] + nums[r] == target:
                count += 1
                l += 1 
                r -= 1
                
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1

            elif nums[l] + nums[r] < target:
                l += 1
                print(l)
            else:
                r -= 1
                print(r)
        
        return count
