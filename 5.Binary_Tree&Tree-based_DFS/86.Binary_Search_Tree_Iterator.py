'''
Use stack, stack[-1] is the next node for in-order traversal
1. use stack to store the trail to left most node
2. hasNext() is the same as check if stack is not empty
3. Next(): return the top of stack, then change to stack to the next state
    - if current node has right subtree (no left tree guaranteed), get its left most node
    - if current node has no right subtree, get the node in trail with first left branch
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left
        # do intialization if necessary

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        if len(self.stack) > 0:
            return True
        
    """
    @return: return next node
    """
    def next(self):
        node = self.stack[-1]
        if node.right != None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        elif node.right == None:
            n = self.stack.pop()
            while self.stack != [] and self.stack[-1].right == n:       # None and [] are different!
                n = self.stack.pop()
            
        return node
