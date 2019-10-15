
'''
Not a good solution: 1. changing i in the for loop. 2. need to take care of target = 's' specifically
'''

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
    
        if target == '':
            return 0
        
        for i in range(len(source) - len(target) + 1):
            j = 0
            while source[i] == target[j] and j < len(target) - 1:
                i += 1
                j += 1
            if j == len(target) - 1 and source[i] == target[j]:
                return i - j
            
        return -1
