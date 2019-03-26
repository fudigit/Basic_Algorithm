'''
BFS traversal
1. for zig (left to right), use left out, right in (deque.popleft() + d.append())
2. for zag (right to left), use right out, left in (right branch go in first, d.pop(), d.appendleft())
Note: in zag step, if queue is empty, return order
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        
        order = []
        
        if not root:
            return order
        
        queue = deque([root])
        while queue:
            zig = []
            for _ in range(len(queue)):
                node = queue.popleft()
                zig.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            order.append(zig)
            
            if queue == deque([]):
                return order
            zag = []
            for _ in range(len(queue)):
                node = queue.pop()
                zag.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            order.append(zag)
            
        return order
            
        
        
        
