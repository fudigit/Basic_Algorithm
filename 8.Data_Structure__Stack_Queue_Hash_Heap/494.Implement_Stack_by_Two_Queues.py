'''
initialize 2 queues, use queue_1 to store all the items, use queue_2 to store previous items from queue_1 when visiting the 'last_in' of queue_1
'''
from collections import deque

class Stack:
    # initialize mandatory attribute, q1 and q2 to self！
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])
    # move all items before lastIn in q1 to q2
    def get_lastIn(self):
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
    # swap q1 and q2
    def swap(self):
        self.q1, self.q2 = self.q2, self.q1
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q1.append(x)
    """
    @return: nothing
    """
    # call method within method
    def pop(self):
        self.get_lastIn()
        self.q1.popleft()
        self.swap()
    """
    @return: An integer
    """
    def top(self):
        self.get_lastIn()
        top_item  = self.q1.popleft()
        self.swap()
        self.q1.append(top_item)
        return top_item
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.q1) == 0
