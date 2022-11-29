class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # result,path = [],[]     # 定义一个一元数组用于存放单层递归的 终止结果。定义一个二元数组 用于存储总的 递归的结果集
        # def backtracking(n, k, startindex):
        #     nonlocal result,path
        #     if len(path) == k:
        #         result.append(path[:])        # 这边第一次的时候我犯了个错误，我之前写的是 result.append(path)，这样结果是：[[],[],[],[],[],[]]
        #                                    # 返回的是path 空数组作为元素返回了，但是我想要的是 path 里面的元素 组成的path 数组的全返回，这样就要返回
        #                                    # path[:], 但是为什么一定要这么写，而不是写成 result.append(path), 我还不是很明白。
        #         return
        #     # 这是递归的终止条件
        #     for i in range(startindex,n+1):    # 第一层递归要执行n-1次，
        #         path.append(i)   # 每一次 递归都预先将 i 的值存入path 数组当中
        #         backtracking(n, k, i+1)   # 每一次 递归都要 从i后面的一个元素遍历起。实质上就是在下一层递归的for 循环上path加上了 i+1 的值进入数组。
        #         path.pop()     # 回溯，每次进行完 递归之后，弹出path 数组的末位值，好进行下一次的递归。
            

                

        # backtracking(n, k, 1)
        # return result
        
        # 方法二：  剪枝优化
        result,path = [],[]     # 定义一个一元数组用于存放单层递归的 终止结果。定义一个二元数组 用于存储总的 递归的结果集
        def backtracking(n, k, startindex):
            nonlocal result,path
            if len(path) == k:
                result.append(path[:])        
                return
            # 这是递归的终止条件
            for i in range(startindex,n-(k-len(path))+2):    # 剪枝操作
                path.append(i)   # 每一次 递归都预先将 i 的值存入path 数组当中
                backtracking(n, k, i+1)   # 每一次 递归都要 从i后面的一个元素遍历起。实质上就是在下一层递归的for 循环上path加上了 i+1 的值进入数组。
                path.pop()     # 回溯，每次进行完 递归之后，弹出path 数组的末位值，好进行下一次的递归。
        
        backtracking(n, k, 1)
        return result