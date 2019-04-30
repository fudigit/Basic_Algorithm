'''
1. add 2 lists together and sort by interval.start. O(Nlog(N))
2. loop through the list and merge the intervals
- not utilizing the sorted(ascending) intervals
- try to do it with merge 2 sorted array
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        
        res = list1 + list2
        res = sorted(res, key = lambda i: i.start)
        
        ans = []
        
        for item in res:
            if ans == []:
                ans.append(item)
                continue
            
            if item.start > ans[-1].end:
                ans.append(item)
                continue
        
            if item.start <= ans[-1].end:
                ans[-1].end = max(item.end, ans[-1].end)
        
        return ans
