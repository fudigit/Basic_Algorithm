class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s or not offset:
            return s
        
        offset = offset % len(s)
        
        tmp = s + s
        # 额外开辟新空间，copy到rotated_s
        rotated_s = tmp[len(s) - offset : len(s) + len(s) - offset]
        
        for i in range(len(s)):
            s[i] = rotated_s[i]
        
        return s
        
