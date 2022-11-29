class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 这道动态规划的题目的第一个思路就是难到我的点。
        # 第一个是想到要用动规，第二个是想到最终结果可以理解为 把数组分为 子集和最相近 的两个集合。
        # 想明白dp[j] 的定义， j是最大容量为j， dp[j] 是 最大容量为j 的时候所能容纳的 最大的价值
        # 然后再完成dp 数组的初始化、
        
        dp = [0]*1501
        target = sum(stones)//2    # 除以2 之后向下取整
        for i in range(len(stones)):   # 先 物品
            for j in range(target,stones[i]-1,-1):    #后背包
                dp[j] = max(dp[j],dp[j-stones[i]]+stones[i])
        return sum(stones)-2*dp[target] 