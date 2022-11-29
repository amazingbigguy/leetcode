class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 有障碍，对应的dp数组 相对应的坐标元素设置为0 就好了
        # 但是要 考虑到 初始化的时候，障碍出现在 上边界和左边界 的情况，需要针对初始化问题 重新书写边界条件
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]    # 定义 dp数组 并且初始化其边界
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1,n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
            else:
                break
        for j in range(1,m):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j-1][0]
            else:
                break
        # 到了这一步 才算完成了初始化
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j]+ dp[i][j-1]
                # else:
                #     continue
        return dp[m-1][n-1]
        