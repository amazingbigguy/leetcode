# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 确定 递归的终止条件(二叉树为空的时候，即是递归终止的时候)
        if not preorder:
            return None
        root = TreeNode(preorder[0])  # 定义、初始化 二叉树根节点

        # 得到根节点的值 来获取其在 中序遍历中的对应元素值的索引，用作分隔左右子树
        seperator_idx = inorder.index(root.val)

        inorder_left = inorder[:seperator_idx]
        inorder_right = inorder[seperator_idx + 1:]

        # 分隔好的对应左右子数组的大小是一样的
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]
        #  这个数组里面的操作我是真的不熟练， 真的烦人

        # 在实现单层递归逻辑
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root