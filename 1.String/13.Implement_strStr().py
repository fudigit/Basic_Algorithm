'''
use i + j to track the char in source, i is the initial index
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
        
        source_len, target_len = len(source), len(target)
        
        for i in range(source_len - target_len + 1):
            j = 0
            while j < target_len:
                if source[i + j] != target[j]:
                    break
                else:
                    j += 1
            
            if j == target_len:
                return i
            
        return -1


'''
Not a good solution: 1. changing i in the for loop. 2. j < len(target) - 1: 意味着target的最后一个元素没有比较，（只到倒数第二个）
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
