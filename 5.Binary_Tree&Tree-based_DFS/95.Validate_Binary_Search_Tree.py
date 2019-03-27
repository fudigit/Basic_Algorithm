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
    
    # 1. Definition: given a tree node, return weather a BT, if yes, BT's max and min
    def divideConquer(self, node):
        # 3. Exist
        if node == None:
            return True, None, None
        # 2. divide and solve
        ## - conquer
        leftIsBST, leftMin, leftMax = self.divideConquer(node.left)
        rightIsBST, rightMin, rightMax = self.divideConquer(node.right)
        
        ## - merge
        # left or right subtree not BST
        if leftIsBST == False or rightIsBST == False:
            return False, None, None
            
        # left max or right min exceed node.val
        if leftMax != None and leftMax >= node.val:
            return False, None, None
        if rightMin != None and rightMin <= node.val:
            return False, None, None
        
        # a valid BSF, get min and max for the current tree
        if leftMin == None:     # no leftMind indicate no left branch
            minNode = node.val
        else:
            minNode = leftMin

        
        if rightMax == None:
            maxNode = node.val
        else:
            maxNode = rightMax
        
        return True, minNode, maxNode
        
        
'''
In order traversal
valid BST: its in order traversal is sorted in ascending order (necessary and sufficient)
1. use lastNode to track the ascending order
2. when is the node value visited and compared? when is the next value assigned?

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
        self.isBST = True
        self.lastNode = None
        self.traverse(root)
        return self.isBST
        
    def traverse(self, node):
        if node == None:
            return
        
        self.traverse(node.left)
        if self.lastNode != None and self.lastNode >= node.val:
            self.isBST = False
            return
        self.lastNode = node.val
        self.traverse(node.right)
        
        
