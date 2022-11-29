class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.used = []    # 采用去重数组来完成 树层去重


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.used = [False]*len(nums)
        nums.sort()    # 使用used 数组进行树层 去重之前，数组nums 必须进行排序
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, start_index):
        self.result.append(self.path[:])
        if start_index >= len(nums):
            return

        for i in range(start_index, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1] == False:
                continue    # 发现重复 元素直接跳到下一个递归 里面
            else:
                self.path.append(nums[i])       
                self.used[i] = True
                self.backtracking(nums, i+1)
                self.path.pop()
                self.used[i] = False