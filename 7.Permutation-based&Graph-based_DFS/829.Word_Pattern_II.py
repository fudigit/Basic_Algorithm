'''
how to determine the pattern corresponds to which word? (ababa -> redblueredbluered, {a:red})
try each word for pattern using dfs!
1. if a pattern is in the mapping, check if pattern matches the head of string
2. if a pattern is not in the mapping, try each word in the remaining string(expect for used word)
    - if the word is alreay a value in mapping, it cannot be value for a second key
3. return true or false for 1 and 2
'''

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        return self.is_Match(pattern, str, {}, set())
        
        
    # try a pattern for each string from left to right, return true if a match   
    def is_Match(self, pattern, str, mapping, used):
        if pattern == '':
            if str == '':
                return True
            return False
        
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if str.startswith(word) is True:
                return self.is_Match(pattern[1:], str[len(word):], mapping, used)
            return False
            
        # when char is not in mapping
        for i in range(len(str)):
            word = str[:i+1]
            # if maping = {a:red}, b can not be red, but can be redb 
            if word in used:
                continue
            
            mapping[char] = word
            used.add(word)
            
            if self.is_Match(pattern[1:], str[i+1:], mapping, used) is True:
                return True
            
            del mapping[char]
            used.remove(word)
            
        
        return False
            
