class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        
        if nums is None:
            return None
        
        if nums == []:
            return 0
        
        nums.sort()
        
        slow = 0
        fast = 0
        
        while fast < len(nums):
            if nums[slow] < nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            else:
                pass
            
            fast += 1
        
        total_uniq = slow + 1
        return total_uniq
        
        
