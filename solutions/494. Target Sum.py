class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #  这道题目 用柜台规划应该 怎么做呢？
        # ok, 我还是想不到如何构造dp[j]  数组
        # 这道题目 让我感觉最妙 的地方就是 还是把求和 target 分成了两坨。
        # 还有一点 就是dp 数组的 递推公式 的物理解释
        sumValue = sum(nums)
        left = (sumValue+target)//2
        if abs(target) >  sumValue or (sumValue+target)%2 == 1:
            return 0
        dp = [0]*(left+1)   #  dp 数组的含义是 数组和为 j 的有dp[j] 中情况
        dp[0] = 1
        for i in range(len(nums)):       #　先遍历　物品，再遍历背包
            for j in range(left, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[left]