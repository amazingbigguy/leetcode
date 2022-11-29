# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        # 使用 递归+插入节点到 叶子节点，将 插入节点的地址传给上一个节点的 孩子节点地址。将上下节点通过地址联系起来。
        # 还需要复习，不是很懂