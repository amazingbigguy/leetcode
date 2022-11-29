class Solution:
    def fib(self, n: int) -> int:
        # a = [0]*31         # 我不明白为什么 这里写成 a = [0]*(n+1) 就会报错啊，错误类型是 IndexError: list assignment index out of range
        # a[0],a[1] = 0,1
        # for i in range(2,n+1):
        #     a[i] = a[i-1]+a[i-2]
        # return a[n]

        # 动态规划的 方法
        if n<2: return n
        a,b,c = 0,1,0     # 我们只需要维护两个斐波拉契数 就行了
        for i in range(1,n):
            c = a + b
            a,b = b,c
        return c

        # # 递归的方法
        # if n < 2: return n
        # return self.fib(n-1)+self.fib(n-2)
