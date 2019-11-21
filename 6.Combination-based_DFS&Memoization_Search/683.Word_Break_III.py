class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        max_lenth, dict_lower = self.init(dict)
        print(max_lenth, dict_lower)
        map1 = {}
        res = self.dfs(s.lower(), 0, dict_lower, max_lenth, map1)
        print(map1)
        return res    
    
    def init(self, dict):
        max_lenth = 0
        dict_lower = set()
        for w in dict:
            max_lenth = max(max_lenth, len(w))
            dict_lower.add(w.lower())
        return max_lenth, dict_lower
        
    # 找以index为开头的所有单词，算以某个单词为开头的所有路径的数量
    def dfs(self, s, index, dict_lower, max_lenth, memo):
        if index == len(s):
            return 1
        
        if index in memo:
            return memo[index]
        
        ans = 0
        for i in range(index, len(s)):
            if i + 1 - index > max_lenth:
                break
            word = s[index:i + 1]
            
            if word not in dict_lower:
                continue

            ans += self.dfs(s, i + 1, dict_lower, max_lenth, memo)
        # 记忆的是什么? 在index位置开头的sentence，所对应的答案
        memo[index] = ans
        return ans
