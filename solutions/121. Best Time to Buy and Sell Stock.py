class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # 可以用贪心法 来实现，也比较好想
        # low = float('INF')
        # result = 0
        # for i in range(len(prices)):
        #     low = min(low,prices[i])
        #     result = max(prices[i]- low, result)
        # return result
        
        # 可以用动态规划的思路来 思考问题
        # 很妙，这边引入了一个 持有股票和不持有股票的概念
        # dp[i][0] 表示第i天 持有股票所获得的最多现金
        # dp[i][1] 表示第i天 不持有股票所获得的最多现金,一开始的现金是0
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0],dp[0][1] = -prices[0],0
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],-prices[i])      # 一开始的递推公式写错了，写成了  dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i]), 但是 本题只是股票买卖只是一次性的，就单次买卖，所以完全不需要加上dp[i-1][1]。
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[len(prices)-1][1]
        
        # 至于用滚动数组节省空间的，我就不写了，下次有机会再来填坑
        
        