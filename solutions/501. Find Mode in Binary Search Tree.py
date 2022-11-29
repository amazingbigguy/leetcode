# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归法 + 用额外的空间（空间换时间的策略）
    def __init__(self):          # 定义几个全局变量
        self.pre = TreeNode()    # 定义一个空二叉树节点
        self.count = 0
        self.max_count = 0
        self.result = []

    # 一次遍历 找到并且返回
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.result
    
    def traversal(self, root):
        if not root:
            return 

        self.traversal(root.left)
        
        if not self.pre:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = root


        if self.count > self.max_count:
            self.result.clear()   # 将结果数组之前存进去的元素清空
            self.result.append(root.val)
            self.max_count = self.count
        elif self.count == self.max_count:
            self.result.append(root.val)

        self.traversal(root.right)

        # 方法二： 迭代法-中序遍历-不使用额外空间，利用二叉搜索树特性 （但是迭代法我一刷的时候不准备做，挖个坑，之后二刷的 时候再做 迭代法。）

