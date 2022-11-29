class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, start_index):
        # 首先判断 终止条件和 输出结果的条件
        if len(self.path) >= 2:
            self.result.append(self.path[:])

        if start_index == len(nums):
            return                     # 这边搞错了，终止条件应该是先输出再 return， 之前写成了 先return 在输出，导致 每一个叶子节点都没有收集到。导致出现了 不容易发现的逻辑 错误。需要谨记。
        
        
        # 定义一个 局部变量 set() 来存储 树层遍历 时候的元素，用于树层 的元素去重。
        usage_list = set()     # 每次进入 下一个树层 遍历的时候， usage_list 会被清空，所以usage_list 是一个完完全全的局部变量
        for i in range(start_index, len(nums)):
            # 判断 去重的条件，即重复 的逻辑判断，并且continue，进入到下一层 树层 递归当中。
            if (self.path and nums[i] < self.path[-1]) or nums[i] in usage_list:
                continue 
            # 即是，要么path 不为空的时候 要存入的元素比 path中最后一个元素的数值要来的小。
            # 要是是，要存入的 元素值 在之前存入过 set() 数组里面，所以不需要再次 考虑
            
            self.path.append(nums[i])
            usage_list.add(nums[i])    # 集合要用 add 的操作了，而不是类似于数组和字符串 的那种 apppend了
            self.backtracking(nums, i+1)
            self.path.pop()