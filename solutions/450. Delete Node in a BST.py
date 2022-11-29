# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 分析删除节点的 5中情况，作为终止条件。递归左右子树 的时候，分别用节点的左右孩子 接住返回的 新的二叉树的 返回节点指针。
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)    # 拿 root 的孩子节点接住 下一层子树返回的节点地址
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)  # 拿 root 的孩子节点接住 下一层子树返回的节点地址
        else:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            return root.right

        return root