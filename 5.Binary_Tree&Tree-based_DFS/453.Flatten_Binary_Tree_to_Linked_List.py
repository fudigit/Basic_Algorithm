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

        
