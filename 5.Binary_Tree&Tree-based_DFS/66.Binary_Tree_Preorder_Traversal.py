"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    
    def preorderTraversal(self, root):
        # why add self in front of result?
        self.result = []
        self.traverse(root)
        return self.result
        
        
    def traverse(self, node):
        if node is None:
            return
        self.result.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)
