class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 完全背包问题，dp[j]   金额为j的前提下，最大有多少种凑齐的方法
        dp = [0]*(amount+1)   # 完成dp 数组的初始化
        dp[0] = 1
        for i in range(len(coins)):  
            for j in range(coins[i], amount+1): 
                dp[j] += dp[j-coins[i]] 
        return dp[amount]
        #　好难，其实不太懂