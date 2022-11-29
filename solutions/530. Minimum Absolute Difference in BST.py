# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 二叉搜索树 使用 中序遍历+递归， 使用双指针和 一个全局变量存储 返回值
        result = float("INF")  # 初始化一个整型 极大值，好吧，没有 int("INF") 这种写法，只有float("INF") 这种写法.
        pre = None  # 全局变量，初始化一个空指针

        def traversal(root):  # 没有返回值，仅仅实现 二叉树的遍历:
            nonlocal pre, result
            if not root:
                return
            traversal(root.left)
            if pre:
                result = min(result, root.val - pre.val)
            pre = root

            traversal(root.right)

        traversal(root)
        return result
