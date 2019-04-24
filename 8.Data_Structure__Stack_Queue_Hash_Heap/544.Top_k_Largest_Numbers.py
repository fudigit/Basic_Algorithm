'''
use min heap to track the top k largest
1. add each number to the min heap
2. if size of min heap exceed k, pop the smallest item with O(logk)
 - the root of min heap is the kth largest number so far!!!
 - pop eliminate the smallest number in k + 1 numbers
 
 O(nlogk)
'''

import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        
        min_heap = [] # min heap to store the top k, eliminate the smallest when exceed k numbers
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        #topK_descend = sorted(min_heap,reverse = True), slightly better time complexity
        topK_ascend = []
        for i in range(k):
            topK_ascend.append(heapq.heappop(min_heap))
        
        topK_descend = topK_ascend[::-1]
            
        return topK_descend
        
