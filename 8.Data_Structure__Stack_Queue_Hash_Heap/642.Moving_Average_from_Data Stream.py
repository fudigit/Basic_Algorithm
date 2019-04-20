'''
how to not calculate a sum every time?
'''

from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.queue = deque([])
        self.sum = 0
        
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        if len(self.queue) < self.size:
            self.queue.append(val)
        elif len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
        self.sum += val
        
        movingAvg = self.sum/len(self.queue)
        
        return movingAvg
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
