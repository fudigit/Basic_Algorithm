class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if not nums:
            return -1
        
        s, e= 0, len(nums) - 1  # starting point of end is len() - 1
        
        while s + 1 < e:
            mid = (s + e)//2
            
            if nums[mid] > target:
                e = mid
            elif nums[mid] < target:
                s = mid
            elif nums[mid] == target:
                s = mid
        
        if nums[e] == target:
            return e
        elif nums[s] == target:
            return s
        else:
            return -1


# 2刷
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if nums == []:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1
        
