
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
            
        
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    '''merge sort'''
    #repeatedly: 
    #  1. split the interval from the middle into 2 
    #  2. merge 2 intervals
    
    def sortIntegers2(self, A):
        # tmp is only used in the merge function to store sorted integers
        # Save time to define it once, and pass as a parameter in the function
        tmp = [None]*(len(A))
        self.mergeSort(A, 0, len(A) - 1, tmp)
        
    def mergeSort(self, A, start, end, tmp):
        
        #base case
        if start >= end:
            return
            
        mid = (start + end)//2
    
        self.mergeSort(A, start, mid, tmp)
        self.mergeSort(A, mid + 1, end, tmp)
        self.merge(A, start, mid, end, tmp)
    
    def merge(self, A, start, mid, end, tmp):
        left_i, right_i = start, mid + 1
        # A and tmp use the same index, so tmp is copy of A with an sorted interval 
        index = start
        
        while left_i <= mid and right_i <= end:
            if A[left_i] <= A[right_i]:
                tmp[index] = (A[left_i])
                left_i += 1
            elif A[left_i] > A[right_i]:
                tmp[index] = (A[right_i])
                right_i += 1
            index += 1
        
        while left_i <= mid:
            tmp[index] = (A[left_i])
            left_i += 1
            index += 1
            
        while right_i <= end:
            tmp[index] = (A[right_i])
            right_i += 1
            index += 1
        
        # update array A within merge function, A stored merged result.
        # tmp stores the 2 merged sorted list, everytime
        for i in range(start, end+1):
            A[i] = tmp[i]
    
    
        
    
