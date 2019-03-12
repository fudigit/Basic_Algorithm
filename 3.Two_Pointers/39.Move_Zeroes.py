'''No Guarantee of minimum operation'''
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # slow pointer vs fast pointer
        # s points to the position where the non-zero integer will be stored
        # f loops through the intger array, when points to non-zero integer, swap value with s
        # this way, the value s being swaped with s is alway a non-zero
        
        s = 0
        f = 0
        end = len(nums) - 1
        
        while f <= end:
            # forward f by 1 until hit end
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
            f += 1

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    
    def moveZeroes(self, nums):
        '''
        2 pointers, right pointer skips zeros
        # right pointer go right stops at where non-zero is found
        # left pointer swap with right every time when right stops, then both move 1 step forward
        '''
        r = 0
        l = 0
        
        while l < len(nums):
            
            # use l to find the first non-zero integer
            while l < len(nums) - 1 and nums[l] == 0:
                l += 1
            
            # swap the non-zero integer with l pointer
            nums[r], nums[l] = nums[l], nums[r]
            
            r += 1
            l += 1
            
            #print(nums, r, l)
            
            
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    
    def moveZeroes(self, nums):
        '''
        2 pointers, minimum operations
        # store non-zero using left pointer, find non-zero using right pointer
        # instead of swap, update left value when left points to non-zero, and to different index
        other than right pointer
        '''
        l, r = 0, 0
        
        while r < len(nums):
            if nums[r] != 0:
                if l != r:
                    # update only when l and r has different index, save operations
                    nums[l] = nums[r]
                # whenever r find a non-zero, l will move
                l += 1
            r += 1
            
        while l < len(nums):
            nums[l] = 0
            l += 1
