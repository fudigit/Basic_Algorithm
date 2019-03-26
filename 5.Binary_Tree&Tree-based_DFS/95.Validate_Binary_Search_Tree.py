'''
devide and conquer
# given each mother node, for it to be a BST:
#   - its left subtree and right subtree are both BST
#   - maximum of the left subtree < node value, and, minimum of the right subtree > node value

Therefore, the recursion function needs to return 3 result, isBTS, maxNode, minNode
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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        
        isBST, minNode, maxNode = self.divideConquer(root)
        
        return isBST
        
    def divideConquer(self, node):
        if node == None:
            return True, None, None
        
        leftIsBST, leftMin, leftMax = self.divideConquer(node.left)
        rightIsBST, rightMin, rightMax = self.divideConquer(node.right)
        print(leftIsBST,rightIsBST)
        
        # left or right subtree not BST
        if leftIsBST == False or rightIsBST == False:
            return False, None, None
            
        # left max or right min exceed node.val
        if leftMax != None and leftMax >= node.val:
            return False, None, None
        if rightMin != None and rightMin <= node.val:
            return False, None, None
        
        # a valid BSF, get min and max for current tree
        if leftMin == None:     # no leftMind indicate no left branch
            minNode = node.val
        else:
            minNode = leftMin

        
        if rightMax == None:
            maxNode = node.val
        else:
            maxNode = rightMax
        
        return True, minNode, maxNode
        
        
        
