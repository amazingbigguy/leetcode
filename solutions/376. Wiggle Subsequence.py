class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 子序列的定义很有意思， 可以删除原数组里面的元素 来构建 子序列
        # 用 贪心算法来做
        if len(nums) == 1:
            return 1
        curdiff = 0    # 当前一对相邻数字的差值 
        prediff = 0    # 之前一对相邻数字 的差值
        result = 1 # 只要是大于等于两个元素的数组，子序列的长度都是 峰值+1
        for i in range(len(nums)-1):
            curdiff = nums[i+1] - nums[i]
            if curdiff*prediff <= 0 and curdiff != 0:  # 差值为0时，不算摆动
                result += 1
                prediff = curdiff
        return result  
#   方法二  动态规划，但是我还没有学到，等以后学到了，二刷的时候再来补齐 这种做法吧。