'''
Use the right end of interval as reference point for k
1. sort the array in asending order
2. use interval's right end as the reference point for k. (k = 1, index = len(A) - 1  
3. return the actual value once kth largest is found
4. len(A) - k is the index of kth largest number
note: after partition, kth largest many belong to left, right inteval, or stand along by itself
'''

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # cases of k that are not considered
        if n > len(nums) or n <= 0:
            return -1
        
        return self.quickSelect(n, nums, 0, len(nums)-1)
    
    def quickSelect(self, k, nums, start, end):
        # base case, would start be greater than end?
        if start == end:
            return nums[start]
        
        # perform a partition with 2 pointers
        l, r = start, end
        pivot = nums[(start+end)//2]

        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                # nums[l] >= pivot and nums[r] <= pivot, swap so both go to the correct sides
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
            #print(nums, 'left',l,'right',r, 'start', start, 'end', end, 'k', k)
        if end - k + 1 >= l:
            # if k is in the left interval, assuming asending array
            return self.quickSelect(k, nums, l, end)
        elif end - k + 1 <= r:
            # the reference point of k is no longer end, but r
            return self.quickSelect(k - (end - r), nums, start, r)
        # when there is element between l and r
        return nums[r+1]
    
    
    
    
'''
Use 0 as the reference point for k. 
1. sort the array in asending order
2. Transform "finding kth largest" to "finding element has index = (len(A) - k)"
use 0 as the reference point for k. (k = 1, index = len(A) - 1).
3. return the actual value once kth largest is found
note: after partition, kth largest many belong to left, right inteval, or bewteen in the 2
'''

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # k is bonded by len(nums) and 1
        if n > len(nums) and n < 1:
            return -1
        
        # finding kth largest is equavelent of finding index of len(A) - k
        return self.partition(len(nums) - n, nums, 0, len(nums) - 1)
        
    def partition(self, k, nums, start, end):
        # start <= k <= end
        # base case
        if start == end:
            return nums[k]
        
        l, r = start, end
        pivot = nums[(start+end)//2]
        
        # partition in asending order
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        print(nums,l,r)
        
        # see which interval k falls in, can be in left, right interval, or right in the middle
        if  k <= r:
            return self.partition(k, nums, start, r)
        elif k >= l:
            return self.partition(k, nums, l, end)
        # r < k < l
        return nums[k]
        
    
    
    
    
