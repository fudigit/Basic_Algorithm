'''
use a minimum heap, similar to LC 544
'''

import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.heap_min = []
        self.size = k
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heapq.heappush(self.heap_min, num)
        if len(self.heap_min) > self.size:
            heapq.heappop(self.heap_min)
    """
    @return: Top k element
    """
    def topk(self):
        # heap_min is a array with min heap structure
        result = sorted(self.heap_min, reverse = True) # O(klogk)
        return result
