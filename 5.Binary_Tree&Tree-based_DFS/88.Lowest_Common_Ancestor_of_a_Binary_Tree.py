'''
# clear definition of recursion & what to return
# 1. given a binary tree with root node, find the LCA of child node A & B
# 1. if LCA if found, return LCA
# 2. if only A is found, return A (root == A)
# 3. if only B is found, return B
# 4. if nothing is found, return None
        
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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # defintion: given root node, return LCA, A, or B node, or None
        if root == None:
            return root
        if root == A or root == B:
            return root
        
        left_return = self.lowestCommonAncestor(root.left, A, B)
        right_return = self.lowestCommonAncestor(root.right, A, B)
        
        if left_return != None and right_return != None:
            return root      #root is LCA
        
        if left_return and right_return == None:
            return left_return
            
        if right_return and left_return == None: 
            return right_return
        
        if left_return == None and right_return == None:
            return None
        
        
