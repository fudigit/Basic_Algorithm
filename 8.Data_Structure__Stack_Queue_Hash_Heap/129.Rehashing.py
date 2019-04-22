'''
1. get the new size after rehashing, initialize the heads and tails of new hash
2. traverse the old hashtable and every Listnode(linkeded list)
3. recalculate the new_hash's index
4. add the node to the new position, if node head exist, add to tail_next
    otherwise, initialize head[i] and tail[i]
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        if not hashTable:
            return
        
        NEW_SIZE = 2*len(hashTable)
        Heads = NEW_SIZE*[None]
        Tails = NEW_SIZE*[None]
        
        curr = index = _node = None
        for first_node in hashTable:
            curr = first_node  #use curr to loop through the linked list
            
            while curr:
                index = curr.val % NEW_SIZE
                _node = ListNode(curr.val)
                
                if Heads[index] == None:
                    Heads[index] = _node
                else:    #Head is not None, add to the tail of linked list(Lint)
                    Tails[index].next = _node
                
                Tails[index] = _node  #Tails[index] always points to the last node
                
                curr = curr.next
                
        return Heads
                    
        
        
