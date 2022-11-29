# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # 方法三：  最直观的方法，用一个数组或者栈来 存储二叉中序遍历的 元素
        # # 然后再把 问题 转化为比较数组元素 是否有序
        # candidate = []

        # def _isvalidBST(root):    # 无需返回值，因为只是实现 二叉树的遍历:
        #     if not root:
        #         return
        #     _isvalidBST(root.left)
        #     candidate.append(root.val)
        #     _isvalidBST(root.right)

        # _isvalidBST(root)
        # for i in range(1,len(candidate)):
        #     if candidate[i-1] >= candidate[i]:
        #         return False
        # return True

        # # 方法二
        # # 递归——标准做法 （这道题目我不是很懂，今天囫囵吞枣做掉，但是明天准备好好复盘）
        # valmax = -float("INF")     # 取得一个 浮点数最小，保证小于最小整型值 -2**31
        # def _isvalidBST(root: Optional[TreeNode]) -> bool:
        #     nonlocal valmax    # 把函数外面的变量导入到 闭包函数（方法）里面来

        #     if not root:
        #         return True
        #         # 根节点为空的 二叉树可以什么类型都是
        #     # 根据 左中右 的中序遍历来做，因为是 判断是否为二叉搜索树，不妨先假设他是，让后拿二叉搜索树的属性去做，来验证。
        #     left = _isvalidBST(root.left)    # 左， 用left 来存储 左子树的bool 值

        #     if valmax < root.val:
        #         valmax = root.val
        #     else:
        #         return False              # 中

        #     right = _isvalidBST(root.right)   # 右

        #     return left and right
        # return _isvalidBST(root)

        # 方法一： 优化双指针，在二叉树里面用双指针，直接判断 二叉树里面 单次操作的节点和 他的上一个遍历的节点的 数值大小。
        pre = None  # 创建一个 全局的空指针 节点 (但是我初始化的是一个空节点，而不是空的二叉树根节点。如何初始化一个空的二叉树的空节点，我尚且不是很清楚)

        def _isvalidBST(root: Optional[TreeNode]) -> bool:
            nonlocal pre
            if not root:
                return True

            left = _isvalidBST(root.left)

            # 判断中的逻辑，实际上从递归的最底层来看是做最左边节点的逻辑判断.但是节点是root，而非root.left，因为第一个开始判断的 节点是左子树最左边的节点，但是实质上 的判断是 单次递归里面的中间节点的逻辑。
            if pre and pre.val >= root.val:  # ⚠️ 注意: Leetcode定义二叉搜索树中不能有重复元素
                return False
            else:
                pre = root  # 用pre 存储当前节点的 地址

            right = _isvalidBST(root.right)

            return left and right  # 左右节点都为真，中间节点才为真

        return _isvalidBST(root)