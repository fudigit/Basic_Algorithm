'''
implement queue with 2 stacks

1. use object, so you have all the basic methods!
2. use class name + () to create a object, otherwise: a = MyQueue_byStack is still a class!
'''
  
class MyQueue_byStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def stack2ToStack1(self):
        while self.s2 != []:
            self.s1.append(self.s2.pop())
        
    # add to stack2
    def push(self, x):
        self.s2.append(x)
        
    # if stack1 is empty, pop all in stack2 into stack1, then pop stack1
    def pop(self):
        if self.s1 == []:
            self.stack2ToStack1()
        head = self.s1.pop()
        return head
    
    # if stack1 is empty, pop all in stack2 into stack1, then peek stack1
    def top(self):
        if self.s1 == []:
            self.stack2ToStack1()
        top = self.s1[-1]
        return top
    
    def isEmpty(self):
        if self.s1 == [] and self.s2 == []:
            return True
        return False
        
q_s = MyQueue_byStack()
q_s.push('1')
q_s.top()
q_s.push(2)
q_s.push(3)
q_s.top()
q_s.pop()
q_s.pop()
q_s.pop()
q_s.pop()
