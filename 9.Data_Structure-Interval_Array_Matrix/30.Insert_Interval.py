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
            
                
