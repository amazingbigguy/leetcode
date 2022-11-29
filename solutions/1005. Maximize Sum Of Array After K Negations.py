class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # nums.sort()   # 先给数组排个序
        # count,sum = 0,0
        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         count += 1    # 统计数组中有多少个负数
        #         nums[i] = -nums[i]
        # nums.sort()   # 再次排序，找到 绝对值后数组的最小值
        # for i in range(len(nums)):
        #     sum += nums[i]
        # if (k-count)%2 == 0:
        #     return sum
        # else:
        #     return sum-2*nums[0]
        # # 这是我第一遍的 代码，里面的错误是 想当然的认为k 值要比 数组中负数多， 实质上就是考虑不周

        # 贪心算法，本题的思路
        # 1、将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
        # 2、从前向后遍历，遇到负数将其变为正数，同时K--
        # 3、如果K还大于0，那么反复转变数值最小的元素，将K用完
        # 4、求和
        nums = sorted(nums, key=abs, reverse = True)   # 将 nums 按照数组元素绝对值大小 从大到小排序
        for i in range(len(nums)):
            if k > 0 and nums[i]<0:
                nums[i] *= -1
                k -= 1
        if k >0:    # 如果 k还有的剩，就完全用在 nums数组最小元素上
            nums[-1] *= (-1)**k
        # 求和
        return sum(nums) 