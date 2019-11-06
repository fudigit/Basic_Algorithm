"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        if not root:
            return []
        
        result = []
        
        self.dfs(root, [], result, target)
        
        return result
        
    def dfs(self, root, path, result, target):
        if not root:
            return
        
        self.find_path(root, path, 0, result, target)
        
        self.dfs(root.left, path, result, target)
        self.dfs(root.right, path, result, target)
    
    def find_path(self, root, path, now_sum, result, target):
        if not root:
            return
        
        now_sum += root.val
        path.append(root.val)
        
        if now_sum == target:
            result.append(path[:])
            
        self.find_path(root.left, path, now_sum, result, target)
        self.find_path(root.right, path, now_sum, result, target)
        
        path.pop()
