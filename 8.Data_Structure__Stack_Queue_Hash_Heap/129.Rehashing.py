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
    
    
    
    
    '''
    only create new hashTable, do not open other space
    '''
    
    # add node to the tail node of linked list: if node links to the next node, point to the next node. 
    #                                            if node.next is None, tail found! add to be the last node
    class Solution:
    def addlistnode(self, node, number):
        if node.next != None:
            self.addlistnode(node.next, number)
        else:
            node.next = ListNode(number)

    # calc index of node.val in the new hashTable, add node into new hashTable
    # if adding the first node, just add, else, find the tail of the linked list.
    def addnode(self, anshashTable, number):
        p = number % len(anshashTable)
        if anshashTable[p] == None:
            anshashTable[p] = ListNode(number)
        else:
            self.addlistnode(anshashTable[p], number)

    # traver each head node in the old HashTable, for each node, traverse the old linked list, add node to the new hashTable
    def rehashing(self,hashTable):
        HASH_SIZE = 2 * len(hashTable)
        anshashTable = [None for i in range(HASH_SIZE)]
        for item in hashTable:
            p = item
            while p != None:
                self.addnode(anshashTable,p.val)
                p = p.next
        return anshashTable
                    
        
        
