# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = 0
        def traversal(root: Optional[TreeNode]):
            nonlocal pre
            # 首先书写终止条件
            if not root:
                return 
            traversal(root.right)
            root.val = root.val + pre
            pre = root.val
            traversal(root.left)
        traversal(root)
        return root
#   函数闭包，但是是一道很好理解的题目。 只要用到双指针就可以了。
