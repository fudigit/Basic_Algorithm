class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        
        # use 3 pointers
        # 2 pointers scan the elements in A and B backwards
        # 1 pointer is used to assign value into A starting from m + n - 1
        
        i = m - 1
        j = n - 1
        index = m + n - 1
        
        print(A, i, j)
        
        # when i < 0 and j >= 0, B still has unassigned elements
        # when i>= 0 and j < 0, B is fully assigned, no need to sort the rest in A
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[index] = A[i]
                i -= 1
            elif A[i] < B[j]:
                A[index] = B[j]
                j -= 1
            
            index -= 1
            
        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1
        
        
        # write your code here
