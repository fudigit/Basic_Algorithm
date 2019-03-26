'''
devide and conqure
1, devide and conqure definition of balanced binary tree:
    - a. left child tree is a balance binary tree, right child tree is a balance binary tree
    - b. if both child tree a balance, their depth different <= 1
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        self.NOT_BALANCED = -1
        
        return self.maxDepth(root) != self.NOT_BALANCED
    
    # 1. return -1 if not balanced, 
    # 2. return depth if balanced(required to compare the depth of left/right child trees )
    def maxDepth(self, node):
        if node == None:
            return 0
        
        leftMax = self.maxDepth(node.left)
        rightMax = self.maxDepth(node.right)
        
        if leftMax == self.NOT_BALANCED or rightMax == self.NOT_BALANCED:
            return self.NOT_BALANCED
        
        if abs(leftMax - rightMax) > 1:
            return self.NOT_BALANCED
            
        return max(leftMax, rightMax) + 1
