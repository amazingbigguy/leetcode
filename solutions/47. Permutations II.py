class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        nums.sort()
        used = [0]*len(nums)
        self.backtracking(nums, used)
        return self.result

    def backtracking(self, nums,used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                continue
            if used[i] == 1:    # 如果 nums[i] 事前已经取过了，那么这里需要 跳过，进入下一个元素的选取。
                continue
            self.path.append(nums[i])
            used[i] = 1
            self.backtracking(nums,used)
            self.path.pop()
            used[i] = 0
