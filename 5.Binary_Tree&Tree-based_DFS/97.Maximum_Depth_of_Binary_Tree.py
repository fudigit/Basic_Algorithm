'''
use prenode traversal
# use a global variable depth to track the deepest tree level reached
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # initialize depth: a instance variable
        self.depth = 0
        self.traverse(root, 1)
        return self.depth
        
    
    def traverse(self, node, curDepth):
        if node == None:
            return
        
        # node is not none, make sure depth track the current deepest
        self.depth = max(self.depth, curDepth)
        self.traverse(node.left, curDepth + 1)
        self.traverse(node.right, curDepth + 1)
