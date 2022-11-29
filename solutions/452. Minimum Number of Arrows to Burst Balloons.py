class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 依然是很巧妙的 贪心算法, 我只是看明白了代码，自己写却是 怎么也写不出来了
        points.sort(key = lambda x: x[0])
        
        result = 1   # 因为 points 数组不为空，所以至少需要来一箭
        for i in range(1,len(points)):
            if points[i][0] > points[i-1][1]:    # 如果前后点完全不沾边，那么就需要再射一箭，把前面的气球打掉
                result += 1
            else:
                points[i][1] = min(points[i][1], points[i-1][1])   # 需要维护 气球的右边界，好进行下一轮 的右边界 的比较
        return result