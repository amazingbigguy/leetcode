class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #  这道题目的 贪心实在是太难了，我觉得就算是 三刷 的时候，依靠我自己的能力也是 无法用贪心写出来的
        result = 0
        minprice = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] >= minprice and prices[i] <= fee + minprice:
                continue   # 不买不卖， 持有阶段
            else:
                result += prices[i] - minprice -fee
                minprice = prices[i] - fee        # 这一步 真的很妙
        return result
# 从代码中可以看出对情况一的操作，因为如果还在收获利润的区间里，表示并不是真正的卖出，而计算利润每次都要减去手续费，所以要让minPrice = prices[i] - fee;，这样在明天收获利润的时候，才不会多减一次手续费！