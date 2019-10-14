# check
# 2 cases: sub palindrome has even length, sub palindrome has odd length. In the even case, left pointer = right pointer - 1



'''
V1. write function to expand from the middle, enumerate odd and even cases
'''
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        longest = ''

        for mid in range(len(s)):
            
            sub_odd = self.middle_expand(s, mid, mid)
            if len(sub_odd) > len(longest):
                longest = sub_odd
            sub_even = self.middle_expand(s, mid, mid + 1)
            if len(sub_even) > len(longest):
                longest = sub_even
                
        return longest
    
    
    def middle_expand(self, s, l, r):
        while l >= 0 and r <= len(s) -1 and s[l] == s[r]:
            l -= 1
            r += 1
        
        l_expand = l + 1
        r_expand = r - 1
        
        return s[l_expand:r_expand + 1]
            
            
            



'''
V2. loop the string 2 times, one assuming odd length, one assuming even length
'''
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        max_len = 0
        max_start = None
        max_end = None
        l_bound, r_bound  = 0, len(s) - 1
        
        # if palindrome odd, loop through the string
        for index in range(len(s)):
            l = r = index

            # expand the current index to its left & right and find the longest palindrom
            while l >= l_bound and r <= r_bound and s[l] == s[r]:
                l -= 1
                r += 1
                
            p_lenth = r - 1 - (l + 1) + 1 # correct? l and r always go out 1 more step
            print(p_lenth, l, r)
            if p_lenth > max_len:
                max_len = p_lenth
                max_start = l + 1
                max_end = r - 1 + 1   # string expression 'abc'[0:3]
        
        # if even, loop through the string
        print('try even')
        for index in range(len(s)):
            l, r = index, index + 1
            while l >= l_bound and r <= r_bound and s[l] == s[r]:
                l -= 1
                r += 1
                
            p_lenth = r - 1 - (l + 1) + 1 # correct? l and r always go out 1 more step
            print(p_lenth, l, r)
            if p_lenth > max_len:
                max_len = p_lenth
                max_start = l + 1
                max_end = r - 1 + 1   # string expression 'abc'[0:3]
        
        return s[max_start:max_end]
