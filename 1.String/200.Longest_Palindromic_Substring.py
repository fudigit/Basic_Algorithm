# check
# 2 cases: sub palindrome has even length, sub palindrome has odd length. In the even case, left pointer = right pointer - 1


class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        l_bound = 0
        r_bound = len(s) - 1
        max_len = 0
        max_start = None
        max_end = None
        
        for i in range(len(s)):
            l = r = i
            while l >= l_bound and r <= r_bound and s[l] == s[r]:
                sub_len = r - l + 1
                if sub_len > max_len:
                    max_len = sub_len
                    max_start = l
                    max_end = r
                l -= 1
                r += 1
                
            max_sub = s[max_start: max_end + 1]
        return max_sub
