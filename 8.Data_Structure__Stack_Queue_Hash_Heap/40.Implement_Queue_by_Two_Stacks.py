'''
1. use s2 to store, FIFO, s2: [1,2,3
2. when pop, dump s2 into s1, then just pop s1, s1: [3,2,1
3. when pop or top if s1 is [], then dump s2 into s1
'''

class MyQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def s2ToS1(self):
        while self.s2 != []:
            self.s1.append(self.s2.pop())
    
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.s2.append(element)
    """
    @return: An integer
    """
    def pop(self):
        if self.s1 == []:
            self.s2ToS1()
        ret = self.s1.pop()
        return ret

    """
    @return: An integer
    """
    def top(self):
        if self.s1 == []:
            self.s2ToS1()
        ret = self.s1[-1]
        return ret
