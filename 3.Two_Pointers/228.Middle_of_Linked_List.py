'''
Find the middle node of a linked list.

Example 1:

Input:  1->2->3
Output: 2	
Explanation: return the value of the middle node.

Example 2:
Input:  1->2
Output: 1	
Explanation: If the length of list is  even return the value of center left one.	

Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?
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
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    
    # solution 1, fast and slow pointer start from node 1
    # Note: to get the Node of Linked List, use a pointer to loop through it
    
    def middleNode(self, head):
        
        fast, slow = head, head
        
        if head is None:
            return None
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            print('slow is %s' % (slow.val),'fast is %s' % (fast.val))
            
        return slow
  
  
  
class Solution2:
    # solution 2: slow starts from ListNode 1, fast starts from ListNode 2
    # odd: 1->2->3->null, fast stops at null
    # even: 1->2->3->4->null, fast stops at the last node

    def middleNode(self, head):
        
        fast, slow = head.next, head
        
        if head is None:
            return None
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            print('slow is %s' % (slow.val),'fast is null = %s' % (fast is None))

        return slow

        
