class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    ###count how many times each letter occurs, even will be palindromes, odd > 1 will give a count - 1 palindrome. Add 1 final count if odd or single has occurred 
    '''O(n) + O(len(letter_dic) + O(1)'''
    ### use dictionary to count how many times each letter appeared
    def longestPalindrome(self, s):
        check_set = []
        
        for i in s:
            if i not in check_set:
                check_set.append(i)
            elif i in check_set:
                check_set.remove(i)
                
        if len(check_set) == 0:
            length = len(s)
        elif len(check_set) >= 1:
            length = len(s) - len(check_set) + 1
        
        return length
            
            
        # write your code here

       # new solution

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        
        single_occurrence = {}
        
        for char in s:
            if char in single_occurrence:
                del single_occurrence[char]
            else:
                single_occurrence[char] = 1
        
        single_count = 0

        for key, value in single_occurrence.items():
            single_count += value
        
        if single_count == 0:
            return len(s) - single_count
        
        return len(s) - single_count + 1
                
