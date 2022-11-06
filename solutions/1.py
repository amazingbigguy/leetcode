# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: [TreeNode], targetSum: int):
        # 先进后出，可以用数组来做栈
        result, path = [], []  # 用path 数组做栈，用result 存储数组path 作为元素输出
        path.append(root.val)
        if not root:
            return []
        self.traversal(root, targetSum - root.val)
        return result

    def traversal(self, node, count):  # path 和 result 都算是函数外的主函数变量，不需要作为外函数的参数, 否则自我调用的时候会覆盖:
        # 因为需要遍历二叉树，所以不需要返回值。只需要在遍历的时候有外部变量（外部数组）一直在记录工作就行了,之后也只需要外部数组、外部变量做输出就行了，递归做纯工具就好了。看作一个单纯的深度遍历就好了。
        # 先判断终止条件
        if not node.left and not node.right:
            if count == 0:
                result.append(path[:])  # 把path 数组中深度遍历 到叶子节点的符合题意的结果输出
            return

            # 分析左右节点的单层递归和回溯逻辑
        if node.left:
            count -= node.left.val
            path.append(node.left.val)
            self.traversal(node.left, count)
            path.pop()  # 后入先出，回溯把尾部元素弹出去
            count += node.left.val
        if node.right:
            count -= node.right.val
            path.append(node.right.val)
            self.traversal(node.right, count)
            path.pop()
            count += node.right.val
        return
a = TreeNode()
b = Solution()
print(b.pathSum(TreeNode([5,4,8,11,None,13,4,7,2,None,None,5,1]),22))