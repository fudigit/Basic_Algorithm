'''
sift up:
1. for every element A[i], compare A[i] and its father node, if A[i] < A[father]:
    Swap with father node(sift up)
2. After swap, compare the siftedup node with the nest father node,
    Until A[father'] > A[father]
'''

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
        
        
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1)//2 # (k-1)//2 and (k-1)//2 give the same result
            if A[k] > A[father]:
                break
            # when A[i] <= A[father]
            tmp = A[k]
            A[k] = A[father]
            A[father] = tmp
            
            k = father # track the index of A[k] after swap

# 2刷
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def sift_up(self, A, new):
        while new != 0:
            father = (new - 1)//2
            if A[new] < A[father]:
                A[new], A[father] = A[father], A[new]
                new = father
            else:
                break
                
    
    def heapify(self, A):
        for i in range(len(A)):
            self.sift_up(A, i)
        
