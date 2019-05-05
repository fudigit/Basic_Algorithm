class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        if nums == []:
            return None
            
        if len(nums) % 2 == 1:
            return getKthNum(nums, len(nums)//2 + 1)
        else:
            median = (getKthNum(nums, len(nums)//2) + getKthNum(nums, len(nums)//2 +1))/2
            return median
            
    # find the 1st num x such that there are >= k nums <= x
    def getKthNum(self, arrays, k):
        start, end = self.getRange(nums)
        while start + 1 < end:
            mid = (start + end)//2
            if self.LsEqMid2dCount(arrays, mid) >= k:
                end = mid
            else:
                start = mid
        if LsEqMid2dCount(arrays, start) >= k:
            return start
        return end
    
    #get min and max of the 2d array
    def getRange(self, arrays):
        min_num = min([arr[0] for arr in arrays])
        max_num = max([arr[-1] for arr in arrays])
        return min_num, max_num

    # count numbers less or equal than mid in the 2d array
    def LsEqMid2dCount(self, arrays, mid):
        count = 0
        for arr in arrays:
            count += self.LsEqMidArrCount(self, arr, mid)
        return count
    # count numbers less or equal than a target in the arr
    def LsEqMidArrCount(self, arr, target):
        if arr == []:
            return 0
        # find the 1st num > target in arr 
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if arr[mid] > target:
                end = mid
            elif arr[mid] < target:
                start = mid
            elif arr[mid] = target:
                start = target
                
        if target[start] > target:
            return start + 1
        elif:
            return end
        
        return len(arr) + 1
