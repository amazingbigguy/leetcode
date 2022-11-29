class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x:(x[0],x[1]))   # 按照左边界 从小到大排序
        # result = []
        # start = intervals[0][0]
        # end = intervals[0][1] 
        # for i in range(1,len(intervals)):
        #     if intervals[i][0] > end:
        #         result.append([start, end])
        #         start = intervals[i][0]
        #         end = intervals[i][1]   
        #     elif intervals[i][1] >= end:  
        #         end = intervals[i][1]   

        # result.append([start,end])
        # return result

        # 标准解法  写个更加干练一些，依然是根据 左边界排序
        intervals.sort(key= lambda x:x[0])
        result = []
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            last = result[-1]     # 把结果数组的最后一个元素取出来
            if last[1] >= intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]    # 更新并且维护 result 数组最后一个元素的 值
            else:
                result.append(intervals[i])
        return result

