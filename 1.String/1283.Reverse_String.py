class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        
        reverse_s = ""
        
        for i in range(len(s)):
            reverse_s = s[i] + reverse_s
            
        return reverse_s
        
