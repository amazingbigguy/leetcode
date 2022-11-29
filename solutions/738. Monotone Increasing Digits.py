class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 贪心 
        a = list(str(n))    # 先将 n 转化为 字符串，在把字符串 转化为 列表。 即使数组 的数据结构，但是里面存储的元素 都是一个一个的字符
        for i in range(len(a)-1, 0, -1):
            if int(a[i]) < int(a[i-1]):
                a[i:] = '9'*(len(a)-i)       # TypeError:　'str' object does not support item assignment
                a[i-1] = str(int(a[i-1])-1)
        return int("".join(a))
