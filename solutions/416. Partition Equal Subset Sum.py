class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 这是一道 01 背包问题
        # if sum(nums)%2 !=0:
        #     return False
        # targetsum = sum(nums)//2    # 数组nums 的和 整除 2，等到 01背包 的目标和值
        # nums.sort()
        # temp = 0
        # for i in range(len(nums)):
        #     temp += nums[i]
        #     if temp > targetsum:
        #         return False
        #     elif temp == targetsum:
        #         return True
        # # 没有考虑到数组中 可能有相同的元素
        

        # 这道题目的 dp 数组我不是很明白 应该如何构造
        # 或者说 我不是很明白 dp[i] 的含义，我有点迷糊
        # 看了 讲解，说是判断弹出 条件是dp[target] == target, 重量和价值是一致的，即是重量 是多少，价值就是多少。通过 重量的限制，限制 取值。
        # dp[j] 代表的是 容量为j 的背包，所能装得下的最大的 价值，因为重量 和价值绑定一致，所以dp[j] 的值一定是小于等于 j，那么 只需要 在 j= targetsum 的时候做判断，j > targetsum 的时候做剪枝 就可以了。
        
        if sum(nums)%2 != 0:
            return False
        targetsum = sum(nums)//2
        dp = [0]*(targetsum+1)       # dp[j]  代表的是容量 为j 的背包 最多能容纳的 价值, 最好覆盖 最大的容量。

        for i in range(len(nums)):    # 物品
            for j in range(targetsum,nums[i]-1,-1):   # 背包容量
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
                if dp[j] == targetsum:
                    return True
        return False