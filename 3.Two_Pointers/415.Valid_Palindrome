class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # r ++ and l++ if not alnum, require right < left during r++ and l--
        # only compare lower case!
        
        if s is None:
            return False
        
        right, left = 0, len(s) - 1
        
        while right < left:
            
            while not s[right].isalnum() and right < left:
                right += 1
            while not s[left].isalnum() and right < left:
                left -= 1
            
            if s[right].lower() != s[left].lower():
                return False
            
            else:
                right += 1
                left -= 1
        
        return True
        
        # write your code here
