class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 目测 是一道挺标准的 动态规划的问题，完全背包+排序问题
        # dp[j] 表示 总和为j 的元素组合的个数
        dp = [0]*(target+1)   #  初始化dp 数组
        dp[0] = 1   # 为了解题设置的 dp[0]，从实际意义上说不通的。
        for j in range(1,target+1):   # 先遍历  背包容量
            for i in range(len(nums)):    # 再遍历 物品，为了实现排序，因为先物品再背包，收集不到（3,1） 的组合。
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[target]