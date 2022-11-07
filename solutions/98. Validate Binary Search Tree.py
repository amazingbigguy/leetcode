# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 递归——标准做法 （这道题目我不是很懂，今天囫囵吞枣做掉，但是明天准备好好复盘）
        valmax = -float("INF")  # 取得一个 浮点数最小，保证小于最小整型值 -2**31

        def _isvalidBST(root: Optional[TreeNode]) -> bool:
            nonlocal valmax  # 把函数外面的变量导入到 闭包函数（方法）里面来

            if not root:
                return True
                # 根节点为空的 二叉树可以什么类型都是
            # 根据 左中右 的中序遍历来做，因为是 判断是否为二叉搜索树，不妨先假设他是，让后拿二叉搜索树的属性去做，来验证。
            left = _isvalidBST(root.left)  # 左

            if valmax < root.val:
                valmax = root.val
            else:
                return False  # 中

            right = _isvalidBST(root.right)  # 右

            return left and right

        return _isvalidBST(root)

        # 还有诸多的不懂和不解，明天在慢慢复看吧
