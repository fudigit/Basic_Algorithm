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
