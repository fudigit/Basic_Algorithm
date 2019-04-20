'''
use array list:
1. push: append()
2. pop: pop()
3. Top: list[-1]
'''

class Stack:
    def __init__(self):
        self.array = []

    """f
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.array.append(x)

    """
    @return: nothing
    """
    def pop(self):
        self.array.pop()
    """
    @return: An integer
    """
    def top(self):
        return self.array[-1] 
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.array) == 0
