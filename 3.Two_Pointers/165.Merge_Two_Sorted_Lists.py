'''
0. How to keep the head of new list? (created head first: real head vsuse dummy)
1. 2 pointers l1 and l2 points to the head of the 2 linked lists
2. 1 pointer cur points to the last position of the merged sorted nodes
    - after each iteration, cur is at the last l1/l2 head being added, so the rest of l1/l2 is also add
3. when 1 list runs out, cur.next = None. Therefore link cur to the head of remaining list
'''



'''
use dummy head
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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        
        dummy = ListNode(0)
        cur = dummy
        
        while l1 is not None and l2 is not None:
            print(cur.val)
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
            
        if l2:
            cur.next = l2
            
        return dummy.next



'''
creat actual head
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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        
        # Null case
        if l1 is None:
            return l2
        if l2 is None:
            return l1
            
        # when not None, head is the node has with smaller val or not null:
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        cur = head
        
        while l1 is not None and l2 is not None:
            print(cur.val)
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
            
        if l2:
            cur.next = l2
            
        return head
