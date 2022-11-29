# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums)-1)


    def traversal(self, nums, left, right)-> Optional[TreeNode]:
        if left > right:  return None
        mid = (left + right)//2      # 向下取整的除法
        root = TreeNode(nums[mid])     # 构造新的 二叉树节点
        root.left = self.traversal(nums, left, mid-1)    # 采用左闭右闭的 数组下标分割 方式分隔数组
        root.right = self.traversal(nums, mid+1, right)
        return root    # 返回二叉树根节点
