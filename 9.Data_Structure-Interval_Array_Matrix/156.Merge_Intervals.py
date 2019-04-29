'''
use lambda function in sort:
sorted(key = None ):
 - key parameter is a function takes 1 argument(element) and return a key for sorting purpose
lambda arg_list: expression of arg_list

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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        intervals_sort = sorted(intervals, key = lambda interval: interval.start) #why this is incorrect? (return [] was not a interval list)
       
        res = []
        last = None
        for item in intervals_sort:
            if last == None or item.start > last.end:
                res.append(item)
                last = item
            elif item.start <= last.end:
                last.end = max(last.end, item.end)
                
        return res
        
