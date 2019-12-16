# 超时解法，用全局变量ans[0]记录是否成功
class Solution:

    def wordBreak(self, s, dict):
        
        ans = [False]
        self.dfs(s, 0, dict, ans)
        return ans[0]
     
    def dfs(self, s, startIndex, dict, ans):
        
        if startIndex == len(s):
            ans[0] = True
            return
        if ans[0] == True:
            return
            
        for i in range(startIndex, len(s)):
            word = s[startIndex:i+1]
            if i == len(s)-1 and word not in dict:  #这部其实没有必要，因为到了for的结尾，自动结束了
                return
            if word not in dict:
                continue
            self.dfs(s, i+1, dict, ans)
