class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 本题是一道 贪心经典区间问题， 值得反复刷

        # 第一个思路就是如果 有重叠的区间，就把区间长度长的区间 删除
        # 转化为 求非交叉分隔 区间的个数
        # 想到要排序， 还要思考是 右排序还是 左排序
        # 这边我们用到右 排序
        intervals.sort(key= lambda x:x[1])    # 按照 右边界 从小到大 排序
        # 然后计算 非交叉分隔区间的个数，再拿总的区间个数 减去 非交叉分隔区间个数就可以了
        count = 1
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>= end:
                count += 1
                end = intervals[i][1]
        return len(intervals) - count
