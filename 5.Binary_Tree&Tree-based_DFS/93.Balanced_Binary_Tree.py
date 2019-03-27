'''
devide and conqure
1, devide and conqure definition of balanced binary tree:
    - a. left child tree is a balance binary tree, right child tree is a balance binary tree
    - b. if both child tree are balanced, their depth different <= 1
Note:
# 1. need to return 2 type of variables: BALANCE and Depth.
#   - trick: set NOT_BALANCED = -1, a special Depth
    

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
    
    # 1. Definition:
    # given a tree node: 1. return -1 if not balanced, return depth if balanced(compare the depth of left/right child trees )
    def maxDepth(self, node):
        # 2. Exist
        if node == None:
            return 0
        # 3. Devide and solve
        # - conquer
        leftMax = self.maxDepth(node.left)
        rightMax = self.maxDepth(node.right)
        # - merge, 2 conditions to be a balanced subtree
        if leftMax == self.NOT_BALANCED or rightMax == self.NOT_BALANCED:
            return self.NOT_BALANCED
        
        if abs(leftMax - rightMax) > 1:
            return self.NOT_BALANCED
        # a valid blanced tree, depth?
        return max(leftMax, rightMax) + 1
