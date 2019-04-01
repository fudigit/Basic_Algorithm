'''
O(h) + O(k)
use O(h) to find the 2 nodes that's closest to the target, use O(k) to find the next k values
1. creat 2 stack, 1 for previous nodes, 1 for next nodes.
    - make sure the top of 2 stacks bounds the target
2. the path to a node is unique, threfore, track the trail of finding target to be stack
3. define iterator to find the next and previous node
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
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None:
            return []
        
        next_stack = self.get_stack(root, target)
        prev_stack = self.get_stack(root, target)
        # make sure: next_stack[-1] > target, prevous_stack[-1] <= target 
        if target >= next_stack[-1].val:
            self.move_next(next_stack)
        else:
            self.move_previous(prev_stack)
        #print(next_stack, prev_stack)
        
        result = []
        for i in range(k):
            if self.next_isCloser(prev_stack, next_stack, target) is True: # next is closer or prev==None
                result.append(next_stack[-1].val)
                self.move_next(next_stack)
            else:
                result.append(prev_stack[-1].val)
                self.move_previous(prev_stack)
        return result
        
    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if target >= root.val:
                root = root.right
            else:
                root = root.left
        return stack
    
    # find the next state of stack, stack[-1] is the next node
    def move_next(self, stack):
        node = stack[-1]
        if node.right is not None:
            cur = node.right
            while cur:
                stack.append(cur)
                cur = cur.left
        elif node.right is None:
            cur = stack.pop()
            while stack != [] and stack[-1].right == cur:
                cur = stack.pop()
        #return stack, no need, because the stack is modified
    
    # find the previous state of stack
    def move_previous(self, stack):
        node = stack[-1]
        if node.left is not None:
            cur = node.left
            while cur:
                stack.append(cur)
                cur = cur.right
        elif node.left is None:
            cur = stack.pop()
            while stack != [] and stack[-1].left == cur:
                cur = stack.pop()  # didn't add () on pop
    
    def next_isCloser(self, prev_stack, next_stack, target):
        if prev_stack == []:
            return True
        if next_stack == []:
            return False
        return target - prev_stack[-1].val > next_stack[-1].val - target
        
    
