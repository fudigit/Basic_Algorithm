"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        if not root:
            return 0
        
        max_sum = [-sys.maxsize]
        self.dfs(root, max_sum, 0)
        return max_sum[0]
    
    def dfs(self, root, max_sum, now_sum):
        if not root:
            return
        
        now_sum += root.val
        max_sum[0] = max(max_sum[0], now_sum)
        
        self.dfs(root.left, max_sum, now_sum)
        self.dfs(root.right, max_sum, now_sum)
    
