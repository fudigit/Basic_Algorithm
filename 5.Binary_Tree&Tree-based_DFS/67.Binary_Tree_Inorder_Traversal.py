# 需要开一个result来保留每一个遇到的节点值
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
    
    def inorderTraversal(self, root):
        
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, root, result):
        if not root:
            return
        
        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)
