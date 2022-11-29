class Solution:
    def rob(self, nums: List[int]) -> int:
        # 这道题目相比还是 动规，但是是环形数组
        # 但是把最后一种情况 分离出去讨论不就行了吗
        # 考虑一个数组不能同时选取头元素和尾元素，可以分为两种情况讨论。
        # 即是不包含尾元素进行数组的选取 + 不包含头元素进行的 数组选取

        if len(nums) ==1:
            return nums[0]
        result1 = self.robrange(nums[1:])    # 不考虑第一个元素
        result2 = self.robrange(nums[:-1])   # 不考虑最后一个元素
        return max(result1,result2)

    def robrange(self,nums):
            if len(nums)==1:
                return nums[0]
            dp = [0]*(len(nums))
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[len(nums)-1]
