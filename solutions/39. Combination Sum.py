class Solution:
    def __init__(self):
        self.result = []
        self.single = []
        self.sum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result.clear()
        self.single.clear()    # 清理全局变量的内存预存值
        

        self.backtracking(candidates, target, 0)
        return self.result

    def backtracking(self, candidates: List[int], target, index):
        if self.sum > target:
            return 
        if self.sum == target:
            self.result.append(self.single[:])    # 因为是shallow copy，所以不能直接传入self.path
# Shallow Copy(浅拷贝)：创建一个新的与原类相同的类，在拷贝过程中，类中的基本类型得到正真的复制，而类中的对象只是实现引用的拷贝。 当我们在新的类中修改了其中的某个对象，这个对象在原始的类中也会得到反映。 原因是我们修改的对象所指向的内存地址是相同的。
            return 
        for i in range(index, len(candidates)):
            self.single.append(candidates[i])
            self.sum += candidates[i]
            self.backtracking(candidates, target, i)
            self.single.pop()
            self.sum -= candidates[i]
        # 美滋滋，这个是完全我自己写出的, 在还没有看carl 的讲解之前自己看题目做出来的。哈哈哈。