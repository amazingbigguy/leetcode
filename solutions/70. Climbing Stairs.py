def climbStairs(self, n: int) -> int:
    # if n < 3:
    #     return n
    # a,b,c = 1,2,0
    # for i in range(2,n):
    #     c = a+b
    #     a,b = b,c
    # return c
    # 改为：一步一个台阶，两个台阶，三个台阶，.......，直到 m个台阶。问有多少种不同的方法可以爬到楼顶呢？
    # 1阶，2阶，.... m阶就是物品，楼顶就是背包。
    # 每一阶可以重复使用，例如跳了1阶，还可以继续跳1阶。
    # 问跳到楼顶有几种方法其实就是问装满背包有几种方法。

    # 那么题目就是一道 完全背包+ 排序的问题。那么就需要先遍历 背包，再遍历物品了
    m = 2
    dp = [0] * (n + 1)  # 确定dp 数组的含义，dp[j] 表示 跳到第j层，有多少种排序方法
    dp[0] = 1
    for j in range(n + 1):  # 因为是完全背包+排序问题，所以要 先遍历 背包，再遍历物品
        for i in range(1, m + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[n]