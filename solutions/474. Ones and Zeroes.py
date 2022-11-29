class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 绝对的好题，因为我还是一点思路 都没有
        # 这道题目 真的太难想了，是两个维度的dp 数组，分别代表01两种重量 维度
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]   #  dp 数组初始化
        
        for str in strs:     # 先遍历物品，物品中 重量有两个维度 
            zerosum = str.count('0')
            onesum = str.count('1') 
            for i in range(m, zerosum -1, -1):    # 在 遍历二维背包的容量，用到遍历的物品 重量。
                for j in range(n, onesum-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zerosum][j-onesum]+1)
        return dp[m][n]