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
    @return: Inorder in ArrayList which contains node values.
    """
    self.result = []
    def inorderTraversal(self, root):
        if not root:
            return
        
        inorderTraversal(root.left)
        result.append(root.value)
        inorderTraversal(root.right)
        
        return self.result
