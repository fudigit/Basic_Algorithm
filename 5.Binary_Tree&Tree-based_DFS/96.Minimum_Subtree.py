'''
divide and conquer
1. the sum of a tree node: sum of left subtree + sum of right subtree + node value
2. global variables: track minimum sum and winnder node
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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # track 2 global variables: minimum sum, root that has the minimum sum

        self.min_sum = None
        self.min_node = None
        self.divideConquer(root)
        return self.min_node
        
    # divide and conquer, return the sum of the subtree, update the minimum sum
    def divideConquer(self, node):
        if node == None:
            return 0
        
        left_sum = self.divideConquer(node.left)
        right_sum = self.divideConquer(node.right)
        
        # check if the node sum is the minimum sum
        node_sum = left_sum + right_sum + node.val
        if self.min_node != None and node_sum < self.min_sum:
            self.min_sum = node_sum
            self.min_node = node
        elif self.min_node == None:
            # min_node starts with None, fill in with the first encounter
            self.min_sum = node_sum
            self.min_node = node
        
        return node_sum
        
        
    
