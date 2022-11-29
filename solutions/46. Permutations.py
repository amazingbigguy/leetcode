class Solution:
    def __init__(self):
        self.result = []
        self.path =[]
        self.used =[]

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 使用used 数组来 做去重的逻辑处理
        self.result.clear()
        self.path.clear()
        self.used = [0]*len(nums)
        self.backtracking(nums, self.used)
        return self.result
    
    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return 
        
        for i in range(len(nums)):
            # 做 去重的判断
            if self.used[i] == 1:
                continue
            self.path.append(nums[i])
            self.used[i] = 1
            self.backtracking(nums, used)
            self.used[i] = 0
            self.path.pop()