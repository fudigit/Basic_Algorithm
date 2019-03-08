class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        # 2 pointers
        # points to the heads of A and B, compare to find the smaller element,
        # and move smaller' pointer to the right  
        
        #time complexicy: O(n + m)
        tmp = list()
        
        m = len(A) - 1
        n = len(B) - 1
        i, j = 0, 0
        
        while i <= m and j <= n:
            if A[i] <= B[j]:
                tmp.append(A[i])
                i += 1
            elif A[i] > B[j]:
                tmp.append(B[j])
                j += 1
        
        while i <= m:
            tmp.append(A[i])
            i += 1
            
        while j <= n:
            tmp.append(B[j])
            j += 1
        
        return tmp
