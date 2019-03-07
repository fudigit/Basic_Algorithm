
'''bubble sort'''

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        if A == []:
            return A
            
        # only need n - 1 times to sort the n-1 largest numbers
        for j in range(len(A) - 1):
           for i in range(len(A) - 1):
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
                else:
                    pass
                    
                    
                    
'''quick sort'''

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    
    def sortIntegers2(self, A):
        if A == [] or A is None:
            return
        
        #call the quickSort function
        self.quickSort(A, 0, len(A) - 1)
        
        
    # quick sort helper function
    def quickSort(self, A, start, end):
        
        # base case, this is important!
        if start >= end:
            return
        
        # Define 2 pointers
        left, right = start, end
        pivot = A[(start + end)//2]
        
        # partition
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
                
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
            
        
        
    
