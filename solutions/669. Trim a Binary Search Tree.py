# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 还是利用递归法来做， 先做左右子树的操作，在做中间节点的操作
        if not root: return None
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right   # 把操作节点的右子树 头结点指针返回到 上一层的 递归中去; 之后有 上一层的 节点指针来接受这个指针返回值
        if root.val > high:
            left = self.trimBST(root.left, low, high) # 同理
            return left
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
            