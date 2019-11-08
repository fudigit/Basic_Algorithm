class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        
        # 1. sort the data first! So the same numbers are together!
        # 2. slow pointer points to the last unique integer, fast pointer loop through the
        #    flat/increasing integers. 
        # 3. If fast > slow integer, Let fast integer be the new last unique integer, slow ++
        
        ''' O(nlog(n)) + O(n)'''
        
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
        

# 2刷
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums:
            return 0
    
        unique = set()
        slow, fast = 0, 0
        
        count = 0
        while fast < len(nums):
            if nums[fast] not in unique:
                unique.add(nums[fast])
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
                count += 1
            else:
                fast += 1
        
        return count
