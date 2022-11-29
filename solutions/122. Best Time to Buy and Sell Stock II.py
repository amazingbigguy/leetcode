class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = 0
        for i in range(len(prices)-1):
            # temp = prices[i+1]-prices[i]
            # if temp > 0:
            #     count += temp
            count += max(prices[i+1]-prices[i], 0)
        return count
    # 依然是 贪心算法，局部最优 推导到 全局最优
    