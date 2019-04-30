'''
min heap

since sorted tuples, O(klog(N)), similar to sorted arrays
 - creat tuple (interval, x, y) to track the location of tuple being pop, 
    and deduct the next interval to push
 - the heap does not support comparison between interval object
    threfore, push (interval.start, x, y) into heap
    when adding interval to the list, still add the interval based on x,y
bug
1. interval object conflicts with heap
2. push interval.start, but add interval object into the list
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        
        # initialing heap
        heap = []
        for index, interval_list in enumerate(intervals):
            if interval_list != []:
                heapq.heappush(heap, (interval_list[0].start, index, 0))
    
        # use min heap to merge k sorted lists
        new = []
        while heap:
            start, i, j = heapq.heappop(heap)
            self.add_interval(new, intervals[i][j])
            if j < len(intervals[i]) - 1:
                heapq.heappush(heap, (intervals[i][j + 1].start, i, j + 1))
        
        return new
        
        # special function to add/merge new interval to list
    def add_interval(self, new, interval):
        if new == []:
            new.append(interval)
            return
        
        last = new[-1]
        if interval.start > last.end:
            new.append(interval)
            return
        
        last.end = max(last.end, interval.end) 
            
