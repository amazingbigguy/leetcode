class Solution:
    def __init__(self):
        self.result = []
        self.path = []


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.result
    



    def backtracking(self, nums, start_index):
        # 终止条件
        self.result.append(self.path[:])
        if start_index >= len(nums):
            return 
        
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()