## list.romove(i) 是O(n),这个方法太慢
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

# 所有能成对子的全部消掉。看最后剩下几个单个的。 
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
        
        single_count = len(single_occurrence)
  
        if single_count == 0:
            return len(s) - single_count
        
        return len(s) - single_count + 1
                

# V3.统计字母出现的次数。偶数次可以形成Palindrome，基数次的偶数部分可以形成。如果有基数次，插一个在正中。
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        freq_hash = {}
        
        for char in s:
            if char not in freq_hash:
                freq_hash[char] = 1 
            else:
                freq_hash[char] += 1
        
        # add all even, for add, add the even part
        # see if there is odd count, if there is, add one in the very end
        length = 0
        odd_count = 0
        
        for key, value in freq_hash.items():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                odd_count += 1

        if odd_count == 0:
            return length
        return length + 1
                

# 数对子，数多少char出现了基数次
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        freq_hash = {}
        
        for char in s:
            if char not in freq_hash:
                freq_hash[char] = 1 
            else:
                freq_hash[char] += 1
        
        
        # count pairs， count odd appearence:
        pairs = 0
        odd = 0
        
        for key, value in freq_hash.items():
            pairs += value // 2
            odd += value % 2
        
        if odd > 0:
            return 2*pairs + 1
        
        return 2*pairs
