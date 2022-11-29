# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 首先书写 终止条件
        if not root:
            return root
        if root == p or root == q:
            return root          # 把 节点地址 返回到上一层
        
        # 后续遍历，左右中
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: return root
        elif left and not right: return left
        elif not left and right: return right
        else:  return None

        # 用到了 后续遍历，但其实是回溯的 思想。
        