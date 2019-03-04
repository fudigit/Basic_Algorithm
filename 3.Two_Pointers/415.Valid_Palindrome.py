class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
        
        # r ++ and l++ if not alnum, require right < left during r++ and l--
        # only compare lower case!
        
    def isPalindrome(self, s):
        
        if s is None:
            return False
        
        left, right = 0, len(s) - 1
        
        while left < right:
            
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            else:
                left += 1
                right -= 1
        
        return True
        
        # write your code here
