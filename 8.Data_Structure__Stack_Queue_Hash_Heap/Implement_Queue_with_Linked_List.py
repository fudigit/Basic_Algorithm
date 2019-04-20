'''
 implement queue with linkd list
''''

class QueueNode:
    def __init__(self, value):
        self.val = value
        self.next = None
    
        
class Queue:
    # create dummy to ease dequeue, create tail to ease enqueue
    def __init__(self):
        self.dummy = QueueNode(-1)
        self.tail = self.dummy
    
    # link the node, move the pointer tail
    def enqueue(self, x):
        self.tail.next = QueueNode(x)
        self.tail = self.tail.next
        
        
    def dequeue(self):
        head = self.dummy.next
        self.dummy.next = dummy.next.next
        
        if self.dummy.next is None:
            self.tail = self.dummy
        return head
        
    def peek(self):
        
        return dummy.next.val
    
    def isEmpty(self):
        if dummy.next == None:
            return True
        return False
