'''
non recursion, find upper and lower bound of target
upper = biggest value <= target
lower = smallest value > target
O(h) = O(h) + O(h)
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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            return root
            
        upper = self.find_upper(root, target)
        lower = self.find_lower(root, target)
        
        if upper is None:
            return lower
        if lower is None:
            return upper
        
        if target - upper >= lower - target:
            return lower
        else:
            return upper
    
        
    def find_upper(self, root, target):
        cur_node = root
        last_node = None
        while root:
            if target >= root.val:
                last_node = root
                root = root.right
            else:
                root = root.left
        if last_node: #last_node is None if all root.val > target
            return last_node.val
        return None
    
        
    def find_lower(self, root, target):
        cur_node = root
        last_node = None
        while root:
            if target < root.val:
                last_node = root
                root = root.left
            else:
                root = root.right
        if last_node:
            return last_node.val
        return None
    
# follow up, do it in one pass
