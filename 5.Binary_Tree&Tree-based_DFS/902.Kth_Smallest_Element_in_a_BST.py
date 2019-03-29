'''
use pre order iterator
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        stack = []
        # get the 1th smallest. Based on def of BST, left most is the smallest
        while root:
            stack.append(root)
            root = root.left
        #print(stack)
        
        step = 1
        while step <= k - 1:
            
            # stack[-1] is the node for current step
            top = stack[-1]
            if top.right is not None:
                suc = top.right
                while suc is not None:
                    stack.append(suc)
                    suc = suc.left
            elif top.right is None:
                pre = stack.pop()
                while stack and stack[-1].right == pre:
                    pre = stack.pop() # cannot exist a right connector relationship, track 2 nodes
            step += 1
            
            #print(stack)
        
        kth_small = stack[-1]
        
        return kth_small.val
