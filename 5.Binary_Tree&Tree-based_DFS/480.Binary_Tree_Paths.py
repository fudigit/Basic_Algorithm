'''
divide and conquer
1. 3 important definitions for recursion

Note:
# 1. '->'.join(path), use -> to join the list of strings in path
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        paths = []
        # 1. definition: all path start from root (can be any node)
        
        # 3. base case/exist
            # None node
        if root == None:
            return paths
            # leaf node
        if root.left == None and root.right == None:
            paths.append("" + str(root.val))
            return paths
        
        # 2. devide and solove
            # conquer
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
            # merge
        for path in left_paths:
            paths.append(str(root.val) + '->' + path)
        
        for path in right_paths:
            paths.append(str(root.val) + '->' + path)
        
        return paths
        
        
