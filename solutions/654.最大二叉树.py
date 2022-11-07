# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 因为是构造二叉树，所以用 递归法的 前序遍历 来实现
        # 因为题目的提示说了，数组的长度不为空，所以终止条件是 数组长度为1 的时候
        if len(nums) == 1:
            return TreeNode(nums[0])
        # 然后严格按照前中后 的遍历顺序来写代码
        node_val = max(nums)
        idx = nums.index(node_val)  # 得到对应的最大值的索引
        node = TreeNode(node_val)

        # 左
        if idx > 0:
            # 构造数组来实现 子数组最大值的寻找
            leftnums = nums[:idx]
            node.left = self.constructMaximumBinaryTree(leftnums)

        # 右
        if idx < len(nums) - 1:
            rightnums = nums[idx + 1:]
            node.right = self.constructMaximumBinaryTree(rightnums)

        return node