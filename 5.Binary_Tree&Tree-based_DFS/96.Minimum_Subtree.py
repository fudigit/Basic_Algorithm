'''
divide and conquer (use global variable)
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
        
# follow up, do not use global variable



'''
divide and conquer (no gloabal variables)
#1. the sum of a tree node: sum of left subtree + sum of right subtree + node value
#2. the recurtion returns 3 variables: min sum, min tree node, and sum
#3. compare to get the min sum in after getting left and right results
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

        minSum, minTree, node_sum = self.divideConquer(root)
        return minTree
        
    # divide and conquer, return the sum of the subtree, update the minimum sum
    def divideConquer(self, node):
        if node == None:
            return sys.maxsize, None, 0
        
        left_minSum, left_minTree, left_sum = self.divideConquer(node.left)
        right_minSum, right_minTree, right_sum = self.divideConquer(node.right)
        
        # compare the left, right subtree, and the mother tree sum to get the minimum sum and treeNode
        sum = left_sum + right_sum + node.val
        if left_minSum == min(left_minSum, right_minSum, sum):
            return left_minSum, left_minTree, sum
        if right_minSum == min(left_minSum, right_minSum, sum):
            return right_minSum, right_minTree, sum
        
        return sum, node, sum
        
        
