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
        


'''
merge by 2 lists for each level, until get 1 list
if each list length is N/k, where N = total number of nodes, 
1. merging 2 list takes 2N/k, merging each level take k*N/k or (k-1)* N/k, about N
2. there are maximum logk levels
O(Nlogk)

merging to left most linked list, 1 by 1
if left most list has length N, rest list has length 1 (merge N and 1 and 1 and ....), takes O(Nk)
if each list length is (N/k)
1. merging takes 2N/k + 3N/k + ... + KN/k

bug
1. if odd number of lists, add the last list is after the for loop!
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
        while len(lists) > 1:
            
            new_lists = []
            for i in range(1, len(lists), 2):
                merged2 = self.merge2Lists(lists[i - 1], lists[i])
                new_lists.append(merged2)
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
            
            lists = new_lists
        
        return lists[0]
        

    def merge2Lists(self, l1, l2):
        dummy = ListNode(0)
        tra = dummy
        curr1 = l1
        curr2 = l2
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tra.next = curr1
                tra = tra.next
                curr1  = curr1.next
            else:
                tra.next = curr2
                tra = tra.next
                curr2 = curr2.next
        if curr1:
            tra.next = curr1
        if curr2:
            tra.next = curr2
        return dummy.next

                
        
