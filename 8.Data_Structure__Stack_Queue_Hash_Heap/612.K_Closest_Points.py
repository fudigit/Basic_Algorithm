'''
use a maximum heap, the root is the kth largest distanced point so far
- the result needs to be sorted by dis, x, y
- use -dis, -x, -y to turn the min heap to a "max heap"
- -dis is the root of min heap, dis is the largest
'''

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        max_heap = []
        
        for point in points:
            dis = self.getDis(point, origin)
            heapq.heappush(max_heap, (-dis, -point.x, -point.y)) # min_heap of -dis is max_heap of dis
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []
        while max_heap != []:
            _, x, y = heapq.heappop(max_heap)
            result.append(Point(-x, -y))      # use Point will be mush faster than [x,y]
        result.reverse()
        
        # max_heap 里的root为dis, p.x, p.y 依次最大的点(-dis, -p.x, -p.y 依次最小的点)
        # 找到了k个距离最小的点，根据dis，p.x, p.y 重新排序
        #tmp = []
        #for item in max_heap:
        #    tmp.append([-item[0], -item[1], -item[2]])
        #tmp = sorted(tmp)
        
        #result = []
        #for item in tmp:
        #    result.append([item[1], item[2]])
        
            
        return result
    
    
    def getDis(self, point, origin):
        dis = (point.x - origin.x)**2 + (point.y - origin.y)**2
        return dis
