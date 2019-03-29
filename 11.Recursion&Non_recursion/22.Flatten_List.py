'''
recursion
1. traverse the nestedList, if a list, traverse items in the list, if integer, append to result
'''

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    res = []
    def flatten(self, nestedList):
        self.res = []
        to_list = [nestedList] #test case has integer
        self.flat(to_list)
        return self.res
        
    # 1. release item if a list, append item to self.res if an integer
    def flat(self, nestedList):
        print(nestedList)
        for item in nestedList:
            # 2. subcase
            if isinstance(item, list):
                self.flat(item)
            # 3. exit
            else:
                self.res.append(item)
            
        return self.res

    
'''
Use stack
pop out the top of the stack
1. if top is a list, release elements, put back to stack
2. if top is an integer, append to the result
stop when stack is []

'''

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        
        stack = [nestedList]
        flattened = []
        
        while stack:
            top = stack.pop()
            if isinstance(top, list):
                for item in top:
                    stack.append(item)
            elif isinstance(top, list) is False:
                flattened.append(top)
        flattened.reverse()
        return flattened
