class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.used = []    # 用一个空的数组 存放 长度为candidate 的bool 值，来记录使用过的元素

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.used = [False]*len(candidates)
        candidates.sort()     #　给数组里面的元素排序
        self.backtracking(candidates, target, 0, 0)
        return self.result

    def backtracking(self, candidates, target, sum, index):
        # 首先书写递归的终止条件
        if sum == target:
            self.result.append(self.path[:])
            return
        if sum > target:
            return 
        
        for i in range(index, len(candidates)):
            if i>0 and candidates[i] == candidates[i-1] and self.used[i-1] == False:  # 这里的False 我大概理解为数值的意思了。
                continue    # 去重的实现，实现树层去重。 进行下一个节点的树层 递归
            self.path.append(candidates[i])
            sum += candidates[i]
            self.used[i] = True
            self.backtracking(candidates, target, sum, i+1)
            self.path.pop()     # 栈的操作
            sum -= candidates[i]
            self.used[i] = False