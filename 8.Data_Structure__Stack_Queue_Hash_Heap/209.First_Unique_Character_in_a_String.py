'''
不使用额外的存储空间。
 - 意思是只开辟一个长度为 26(letter) or 256(char)
 - constant length required, not related to len(str)
Follow up: 960. First Unique Number in Data Stream II

'''

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        count_dict = {}
        
        for c in str:
            if c not in count_dict:
                count_dict[c] = 0
            count_dict[c] = count_dict[c] + 1 
        
        for c in str:
            if count_dict[c] == 1:
                return c
