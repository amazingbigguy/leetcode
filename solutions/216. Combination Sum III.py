class Solution:
    def __init__(self):     # 定义一元数组和二元数组的全局变量
        self.result = []
        self.path = []      
        self.sum = 0

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 类似于 77的写法，定义两个全局变量用于存储 单次递归 的 结果和 符合条件的 结果集
        # 然后书写 元素加入 path 的条件，剪枝的操作，我准备之后在写了。
        self.backtracking(k, n, 1)
        return self.result

    def backtracking(self, k, n, startindex):
        # 书写终止条件
        if self.sum > n:
            return        # 剪枝操作，如果单挑路径的累加值sum大于 目标值n，那么i 之后的递归就不用进行了。直接进行 上一层递归的判断，即使开始回溯。开始判断i 之前的 递归 逻辑判断。    （这是基于和、数值和判断的剪枝）
        if len(self.path) == k:
            if self.sum == n:
                self.result.append(self.path[:])
            return 
        
        for i in range(startindex, 11-(k-len(self.path))):     # 关于k 的剪枝 操作，保证剩余的 元素 数量至少等于 k
            self.sum += i
            self.path.append(i)
            self.backtracking(k, n, i+1)
            self.path.pop()
            self.sum -= i

    # 但是其中蕴含很多不需要遍历的情况，我需要剪枝优化