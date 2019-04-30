'''
merge backwards on A, add the bigger of A and B
'''
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i = m - 1
        j = n - 1
        pos = m + n - 1   # m + n positions in A, therefore [1,2,5] 3 [3,4] 2
        
        while j >= 0:
            if i >= 0 and A[i] >= B[j]: # only add A[i] when A[i] exist and bigger
                A[pos] = A[i]
                i -= 1
            elif i < 0 or A[i] < B[j]:
                A[pos] = B[j]
                j -= 1
            pos -= 1
            
'''
use 2 while solution
'''

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i = m - 1
        j = n - 1
        pos = m + n - 1   # m + n positions in A, therefore [1,2,5] 3 [3,4] 2
        
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[pos] = A[i]
                i -= 1
            elif A[i] < B[j]:
                A[pos] = B[j]
                j -= 1
            pos -= 1
            
        while j >= 0:
            A[pos] = B[j]
            j -= 1 
            pos -= 1
            
        # no need for while i >= 0, since A is already sorted
