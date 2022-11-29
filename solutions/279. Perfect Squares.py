def numSquares(self, n: int) -> int:
        # 这道题目可以用 动态规划来做
        # 是完全背包+组合问题
        # dp[j] 表示 和为j 的完全平方数的最少数量为dp[j]
        dp = [10**4]*(n+1)
        dp[0],dp[1] = 0,1
        nums = [i**2 for i in range(1, n+1) if i**2 <= n]
        
        for i in nums:
            for j in range(i, n+1):
                dp[j] = min(dp[j], dp[j-i]+1)   # 一开始的时候 我的递推公式少加了一个1，是我忘记了dp数组的含义导致的。
        return dp[n]
        # 这道题目的动态规划 太容易超时了。leetcode 的超时设置 好像是10s