class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        # dp[i][j]存当前substring: s[i:j+1]里最长的Palindromic Subsequence的长度
        # dp[i][j]转移方程: 
        # - if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
        # - if s[i] != s[j]: dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        dp = [[1]*len(s) for _ in range(len(s))]
        
        # fill string length = 2
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                
        # 由短序列的LPS长度推导出长序列的LPS长度。要注意遍历三角矩阵i,j的设定和边界
        # gap 是substring头尾index的差值，看作是头尾之间的距离
        for gap in range(2, len(s)):           
            for i in range(len(s) - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                elif s[i] != s[j]:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][len(s)-1]
