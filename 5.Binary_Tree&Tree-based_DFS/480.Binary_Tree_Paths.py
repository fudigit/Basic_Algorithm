'''
divide and conquer
1. 3 important definitions for recursion
2. How to track all the path? For each function call, use a new list to store all the paths.

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
            paths.append(str(root.val) + "")
            return paths
        
        # 2. devide and solove
            # conquer
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
            # merge
        for path in left_paths:      #for leave node: left_paths is [], nothing is appendedd to paths
            paths.append(str(root.val) + '->' + path)
        
        for path in right_paths:
            paths.append(str(root.val) + '->' + path)
        
        return paths

    
    
'''
pre order traversal
1. 3 important definitions for recursion
2. define funciton to find all paths starting from a node

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
        result = []
        if root == None:
            return result
        
        self.dfs_findPath(root, [str(root.val)], result)
        return result
        
    # given previous path and current node, 
    def dfs_findPath(self, node, path, result):

        if node.left == None and node.right == None:
            result.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.dfs_findPath(node.left, path, result)
            path.pop()
            
        if node.right:
            path.append(str(node.right.val))
            self.dfs_findPath(node.right, path, result)
            path.pop()
