class Solution:
    def jump(self, nums: List[int]) -> int:
        # 这道题目的贪心算法 还是比较难易想的，对于数学的理解比较重要。需要 一定的 代码熟练度
        # 还是很巧妙的
        curcover = 0
        nextcover = 0
        step = 0
        for i in range(len(nums)):
            nextcover = max(nextcover, i+nums[i])    # 更新 在curcover 覆盖的范围内 最远的 nextcover 所能跳到的地 索引下标
            if i == curcover:   # 在i 迭代到 curcover 索引 之前，都不进入这个if 判断，而是一直迭代 nextcover 的范围。
                if curcover == len(nums)-1:
                    break
                else:
                    step += 1
                    curcover = nextcover
                    if nextcover >= len(nums)-1:
                        break     # 为了下一层迭代的时候保证 curcover 不会超过索引范围。
        return step
        # 方法二 今天下午心情有点焦躁，看的不是很近去，就算了。下次状态好的时候再来理解一下。
        
            