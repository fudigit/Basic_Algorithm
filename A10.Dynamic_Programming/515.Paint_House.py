#考虑以下：
# 设定状态，dp
# 状态如何转移
# 边界
# 答案

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        if not costs:
            return 0
        # df[i][j] 表示第i个房屋是j色，前i个房屋总价的最小值
        dp = [[float('inf')]*3 for _ in range(len(costs))]
        
        # 一开始的3个房屋最小值已经确定
        dp[0] = costs[0]
        
        # 由前i-1总价的最小值，来求加入下一个房子以后的总价最小值(对每个i只有两个选项)
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        
        return min(dp[-1])
