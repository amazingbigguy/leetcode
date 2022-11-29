class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 用二维dp数组 来做状态转移 的动态规划
        # 如何定义一个 规定大小的 空的二维数组呢？
        dp = [[1 for i in range(n)] for j in range(m)]   # 先定义 一行，在把 m 行定义完
        # 顺便还完成了 对于两条边的初始化
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        