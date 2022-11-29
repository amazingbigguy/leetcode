class Solution:
    def numTrees(self, n: int) -> int:
        # 这道题目 就更加懵逼了，本来就 不熟悉二叉搜索树，还要计算 符合题意的种类......
        # 这道题目的难点在于要能想到用 动态规划，也需要有 从问题中抽象出 递归公式的能力
        
        dp = [0]*(n+1)    # 初始化 dp数组
        dp[0],dp[1] = 1,1   # i 个节点 对应 最大有dp[i] 种 二叉搜索树
        # 从dp[3] = dp[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]   找到规律
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n] 