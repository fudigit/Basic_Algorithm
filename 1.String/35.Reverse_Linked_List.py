"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        
        prev = head
        cur = head.next
        
        while cur.val
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        head.next = None
        
        return
        
