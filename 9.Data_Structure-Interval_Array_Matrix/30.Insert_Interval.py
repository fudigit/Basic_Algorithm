'''
first trail
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
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        for i in range(len(intervals)):
            if intervals[i].start > newInterval.start:
                intervals.insert(i, newInterval)
                break
        if intervals[-1].start <= newInterval.start:
            intervals.append(newInterval)
        
        answer = []
        last = None
        for item in intervals:
            if last == None or last.end < item.start:
                answer.append(item)
                last = item
            else:
                last.end = max(last.end, item.end)
        return answer
            
  
'''
shorter version, finding where to insert at once
1. find where to insert based on start, use insert to insert the interval
2. merge the intervals if intersection exists
    - create a new answer list
    - loop through the old interval, record last interval to see if intersection with the next interval

O(n) to insert the interval, O(n) to merge the intervals
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
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        index = 0 
        while index < len(intervals) and intervals[index].start < newInterval.start:
            index += 1
        intervals.insert(index, newInterval)
        
        ans = []
        last = None
        for item in intervals:
            if last == None or item.start > last.end:
                ans.append(item)
                last = item
            # if intersection, merge the intervals! last interal remains the same!
            elif item.start <= last.end:
                last.end = max(item.end, last.end)

        return ans
