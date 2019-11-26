"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# 实际上移动的就是prev和cur, after的作用是把下一个node拿到，否则cur → prev以后，就拿不到下一个node
# 指针是在reference node，然后把node之间的指向做出改变
# 注意最后停下来，看的是cur变成了None。但表头则变成了prev
# None,   1 -> 2 -> 3 -> None
#  ↑      ↑    ↑
#  prev  cur  after

# after = cur.next
# cur.next = prev
# prev = cur
# cur = after

# None <- 1,   2 -> 3 -> None
#         ↑    ↑    ↑
#        prev cur  after

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        prev = None
        cur = head
        print(cur.val)
        
        while cur:
            #print(cur.val, prev)
            after = cur.next
            cur.next = prev
            
            prev = cur
            cur = after
            #print(cur, prev.val)
        return prev
