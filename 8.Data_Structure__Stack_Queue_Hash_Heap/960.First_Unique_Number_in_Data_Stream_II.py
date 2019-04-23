'''
add
if the number has been visited, return, don't add anything
if the number has never been added twice, and not in linked list, add to the end of the linked list
if the number hsa never been added twice, and in the linked list, remove from linked list, add to the set of twiced added.
firstUnique()
return the head of linked list
'''

class LinkedNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class DataStream:
    def __init__(self):
        self.head = LinkedNode(0)
        self.tail = self.head
        self.dup_set = set()
        self.numToPrev = {}
    
    # dummy -> prev -> 2 -> ..., add(2)
    def remove_linkedNode(self, num):
        prev = self.numToPrev[num]
        prev.next = prev.next.next
        del self.numToPrev[num]      # remove the numToPrev of num
        
        # change the numToPrev of the new node linked
        if prev.next != None:
            self.numToPrev[prev.next.val] = prev
        elif prev.next == None:
            self.tail = prev
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):     # if the num has been visted twice
        if num in self.dup_set:
            return
        if num in self.numToPrev:   # if the num is in the linked list
            self.remove_linkedNode(num)
            self.dup_set.add(num)
            return
        # add node to the tail
        new_node = LinkedNode(num)
        self.numToPrev[num] = self.tail      # the Prev is tail
        self.tail.next = new_node
        self.tail = new_node
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if self.head.next != None:
            return self.head.next.val
        return False
