# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 这道题目用到了 二叉树的后续遍历和 dp 数组的理解
        # dp 是一个长度为2的数组，dp[0] 代表不偷当前节点的 能偷到的最大金额，dp[1] 表示偷当前节点所能 偷到的最大金额
        result = self.robtree(root)
        return max(result)

    def robtree(self, root):
        if not root:
            return [0,0]
        
        # 用到后序遍历
        left = self.robtree(root.left)
        right = self.robtree(root.right)

        # 判断单层循环的逻辑,判断root节点的值到底是偷还是不偷
        val0 = max(left[0],left[1])+max(right[0],right[1])
        val1 = root.val+left[0]+right[0]   # 中间节点偷的情况
        return [val0,val1]