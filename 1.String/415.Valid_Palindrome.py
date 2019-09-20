'''
1. apply a sub while loop and 2 pointers to skip the non alphanumeric items 
    - in the sub while loop, make sure left pointer < right pointer, so don't go out of range
'''

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True
