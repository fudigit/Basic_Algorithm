'''
For each level, add value for each node, and expand the son nodes for the next level
1. Use deque to build a queue, right in, left out

Time: Loop through n nodes, therefore O(n)
Space: Store n nodes in queue, therefore O(n)
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# import deque
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # if root is not none, 'if' converts object to boolean
        if not root:
            return []
        
        # use deque for queue, put root into the queue
        queue = deque()
        queue.append(root)
        
        # list to store result
        result = []

        # for each level of the binary tree, expand the next level
        while bool(queue):
            list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                list.append(node.val)
                
                if bool(node.left):
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list)
                    
        return result
