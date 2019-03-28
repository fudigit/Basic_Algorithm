'''
1. track the lca(may be none), as well as if A, B exist
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.findLCA(root, A, B)
        if a and b:
            return lca
        return None
        
    def findLCA(self, root, A, B):
        if root is None:
            return False, False, None
        
        left_a, left_b, left_node = self.findLCA(root.left, A, B)
        right_a, right_b, right_node = self.findLCA(root.right, A, B)
        
        # update if A and B is found
        a = left_a or right_a or root == A 
        b = left_b or right_b or root == B
        
        # exist, when node A or B is countered, return the node
        if root == A or root == B:
            return a, b, root
            
        if left_node and right_node:
            return a, b, root
        if left_node:
            return a, b, left_node
        if right_node:
            return a, b, right_node
        if not left_node and not right_node:
            return a, b, None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
