'''
Divide and conquer
Definition: restructure the tree/subtree(), return the last node in preorder
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if root == None:
            return root
        
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        
        # restructure
        if left_last != None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        # return last node. (exists right branch, no right branch but left branch, leaf node)
        if right_last != None:
            return right_last
        
        if left_last != None:
            return left_last
            
        if right_last == None and left_last == None:
            return root
            
            

'''
in place, this requires extra log(h) memory due to recursion
# trim the right branch, so linking node to the right of last_node does not change right branch 
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    last_node = None
    
    def flatten(self, root):
        if root == None:
            return
        
        if self.last_node != None:
            self.last_node.left = None
            self.last_node.right = root
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)




'''
Create a new linked list using new TreeNodes
1. create a dummy node and a cursor node points to dummy node
2. preorder traverse the binary tree:
- for each node, link a new TreeNode to the cursor node
- move cursor node to the right
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    
    def flatten(self, root):
        if not root:
            return root
        # dummy node ahead of root node, and cursor node points to dummy node
        dummyNode = TreeNode('dummy') 
        self.curNode = dummyNode
        self.traverse(root)
        
        # modify root left, and root right
        root.left = None
        root.right = dummyNode.right.right
        
    def traverse(self, node):
        if node is None:
            return
        
        self.curNode.right = TreeNode(node.val)
        self.curNode = self.curNode.right
        self.traverse(node.left)
        self.traverse(node.right)

        
https://www.techiedelight.com/clone-given-linked-list/
        
