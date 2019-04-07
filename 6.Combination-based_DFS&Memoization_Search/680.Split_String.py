'''
1. use dfs find to all paths of spliting 1/2, track the stringList
2. in each split, either split 1 or 2 characters. Then perform split on the remaining string
3. when there is no remaining string, return the stringList
O(2^n * n) for cutting 1 character, O(2^(n/2) * n/2) for cutting 2 characters
'''

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        results = []
        if s is None:
            return results
        self.dfs_split(s, [], results)
        
        return results
        
    
    # find all 1,2 characters splits on s, the stringList is what's already splitted
    def dfs_split(self, s, stringList, results):
        # exit
        if s == '':
            results.append(list(stringList))
            return
        
        for i in range(1,3):
            if i > len(s[:i]): # if s is not long enough to have 2 characters splitted out
                return
            
            cut_string = s[:i]
            stringList.append(cut_string)
            self.dfs_split(s[i:], stringList, results)
            stringList.pop()
            
        
