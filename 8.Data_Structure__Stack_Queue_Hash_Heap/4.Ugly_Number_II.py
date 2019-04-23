'''
heappush(heap, item), log(n)
heappop(heap), log(n)

create a list with heap structure to always give the smallest value
1. pop the smallest from heap, time with [2,3,5]
 - the nth pop will be the nth smallest number
2. if the product is not added to heap, add to heap

O(n * logn), given n iterations, each iteration has a heappop and up to 3 heappush
'''
import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        visited = set([1])
        heap = [1]
        
        for i in range(n):
            val = heapq.heappop(heap)   # val is the smallest for the current heap
            for multiplier in [2, 3, 5]:
                prod = val*multiplier
                if prod not in visited:
                    visited.add(prod)
                    heapq.heappush(heap, prod)
    
        return val
        
