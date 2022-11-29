class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # 这道贪心算法的题目也很妙，我大概能理解 贪心算法的 意思了。 我能感觉的到，贪心算法 使用的时机， 感觉像是通过转化问题，从而能以计算机 表示的方式 简化问题。有点像从 理解题意 的角度去简化、去剪枝。
        # cover = 0
        # for i in range(cover+1):   # 通过不断 更新cover 的值，来不断的 推动for循环的进行。
        #     cover = max(cover, i+nums[i])     # 看看选取 到每一个元素所能跳跃覆盖到的范围，然后不断的更新 跳跃能覆盖的范围。
        #     if cover >= len(nums)-1:
        #         return True
        # return False
        #  # python不支持动态修改for循环中变量,使用while循环代替。 我说为什么 我和C++的代码写的一样的，但是我的python 却 运行不正确呢！

         
        cover,i = 0,0
        while i <= cover:   # 通过不断 更新cover 的值，来不断的 推动for循环的进行。
            cover = max(cover, i+nums[i])     # 看看选取 到每一个元素所能跳跃覆盖到的范围，然后不断的更新 跳跃能覆盖的范围。
            if cover >= len(nums)-1:
                return True
            i += 1
        return False