'''
linked list: node.key, node.value, capacity
hash {},  node.key -> prev node 
'''

class LinkedNode:
    def __init__(self, key = None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
        
    # add the node to the tail
    # tail -> node, hash[node.key] => tail node, and point tail the last node
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    # change 'prev -> node -> next -> ... -> tail'
    # to 'prev -> next -> ... -> tail -> node', along with the hash[key] impacted
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        # node is not at tail node
        prev.next = node.next
        if node.next != None:
            self.hash[node.next.key] = prev # hash from next.key to prev node
            node.next = None
            self.push_back(node)
            
    def pop_front(self):        #remove the head node, not the dummy node
        del self.hash[self.head.next.key]   # remove from mapping from hash table
        self.head.next = self.head.next.next # dummy -> head -> next, change to dummy -> next
        self.hash[self.head.next.key] = self.head
        
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.val
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, val):
        if key in self.hash:   # key is in hash
            self.kick(self.hash[key])
            self.hash[key].next.val = val # now hash[key] is the second last node
        else:                   # key is not in hash, add!
            self.push_back(LinkedNode(key, val))  # add new node to the tail
            if len(self.hash) > self.capacity:    # if lenth exceed capacity, pop the head node
                self.pop_front()
            

