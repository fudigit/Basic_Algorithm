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
    def enqueue(self, val):
        node = QueueNode(val)
        self.tail.next = node # tail.next = is to link the node
        self.tail = self.tail.next  # tail = is to point to a different node
        
    # pop the head, return the value of head
    def dequeue(self):
        head = self.dummy.next
        self.dummy.next = self.dummy.next.next
        
        if self.dummy.next is None:
            self.tail = self.dummy
        return head.val
        
    def peek(self):
        return self.dummy.next.val
    
    def isEmpty(self):
        if self.dummy.next == None:
            return True
        return False
        
q = Queue()
q.enqueue('111')
q.peek()  
q.enqueue('test node value')      
q.peek()
q.dequeue()
q.peek()
q.dequeue()
q.isEmpty()
        
        
