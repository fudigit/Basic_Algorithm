'''
1. add 2 lists together and sort by interval.start. O((n+m)*log(n+m))
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
    
 
'''
O(log(n + m))

since the 2 list of intervals are already sorted, similar to merge 2 sorted array
difference:
- instead appending the smaller to the merged array, now adding the interval to the list
- the interval to be added can/can't intersect with the last interval, therefore creat a interval add function

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
        
        new = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i].start <= list2[j].start:
                self.add_interval(new, list1[i])
                i += 1
            else:
                self.add_interval(new, list2[j])
                j += 1
        while i < len(list1):
            self.add_interval(new, list1[i])
            i += 1
        while j < len(list2):
            self.add_interval(new, list2[j])
            j += 1
        return new
        
    def add_interval(self, new, interval):
        if new == []:
            new.append(interval)
            return
        last = new[-1]
        if interval.start > last.end:
            new.append(interval)
            return
        last.end = max(interval.end, last.end)
