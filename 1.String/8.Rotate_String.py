'''
教训:
1. list slice那一段，搞不清楚，
2. python list slice的起点和终点怎么写搞不清楚
3. 不同变量指向同一个mutable object，改变这个mutable object随即改变所有变量
'''
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
        
