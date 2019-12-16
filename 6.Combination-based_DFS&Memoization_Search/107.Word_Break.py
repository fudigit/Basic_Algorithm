#V1. DFS + Memoization,需要加大recursion limit
import sys
sys.setrecursionlimit(100000000)
class Solution:
    def wordBreak(self, s, dict):
        memo = {} # index: false
        max_len = -1
        for word in dict:
            max_len = max(max_len, len(word))
        ans = self.dfs(s, 0, dict, memo, max_len)
        return ans
        
    def dfs(self, s, startIndex, dict, memo, max_len):
        if startIndex == len(s): 
            return True
            
        if startIndex in memo: # 如果在memo里, 说明以starIndex开头的单词not breakable
            return False  # 避免冗余计算
            
        for i in range(startIndex, len(s)):
            if i - startIndex + 1 > max_len:
                break
            word = s[startIndex:i+1]
            #print(i, word)
            if word not in dict:
                continue
            # if word is found in dict, start from next letter
            res = self.dfs(s, i+1, dict, memo, max_len)
            if res == True:
                return True
        
        memo[startIndex] = False
        return False
        


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
            if i == len(s)-1 and word not in dict:  #这步多此一举。到了for的结尾，没找单词，自动会结束
                return
            if word not in dict:
                continue
            self.dfs(s, i+1, dict, ans)
