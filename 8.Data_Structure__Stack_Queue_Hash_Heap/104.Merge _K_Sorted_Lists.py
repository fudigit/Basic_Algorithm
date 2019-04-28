'''
v1. use min heap
1. Add node head of each ll into to min heap
2. pop the root of min heap to be the next mode of the merged list (push root.next into min heap)
3. create index to avoid node comparison in head, when value tie
O(N*logk)
'''


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        self.index = 0
        
        # put all nodes into min heap
        min_heap = []
        for node_head in lists:
            if node_head != None:
                self.heappushNode(min_heap, node_head)
        
        # keep add the root of the min heap into the merged list, push the next node into min heap
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            root = heapq.heappop(min_heap)[2]
            curr.next = root
            curr = curr.next
            
            if root.next != None:
                self.heappushNode(min_heap, root.next) # note, merged list has a unwanted 'tail'
        
        return dummy.next
        
    def heappushNode(self, heap, node):
        self.index += 1 # so when node.val tie, no need to compare nodes
        heapq.heappush(heap,(node.val, self.index, node))
