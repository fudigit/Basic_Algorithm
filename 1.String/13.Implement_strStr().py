class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        
        for i in range(len(source)):
            j = 0
            while source[i] == target[j] and j < len(target) - 1:
                i += 1
                j += 1
            if j == len(target):
                return i - len(target) + 1
            else:
                pass
            
        return -1
            
