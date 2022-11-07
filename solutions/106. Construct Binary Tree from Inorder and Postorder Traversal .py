# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 前序遍历数组和后续遍历数组 不能确定唯一的一颗二叉树。但是前+中 或者 中+ 后 可以确定唯一的一颗二叉树
        # 因为有中节点做分隔，做数组分隔。
        # 这其中涉及到的数组的数值和索引的相关知识还是值得我 再度深入学习的

        # 首先确定终止条件, 即是树为空
        if not postorder:  # 判断 后序遍历的数组为空的情况
            return None

        rootval = postorder[-1]  # 确定根节点（中心节点的数值）
        root = TreeNode(rootval)  # 声明定义初始化 根节点

        # 在中序遍历 的结果数组中 寻找和中节点 相同值的元素索引
        seperator_idx = inorder.index(rootval)  # 这个数组的命令我还是第一次见到，觉得很有用，也很秒。实现了已知数值元素值，寻找并返回元素下引的 功能。

        # 分隔数组，新建新的数组。 后序遍历的后左组的 大小和中序遍历 中左组的 数组大小是一样的，这是题目本身决定的。
        inorder_left = inorder[
                       :seperator_idx]  # 把原数组第一个元素到 seperator_idx 索引的前一个元素赋给新数组，正好 seperator_idx 数值 个元素. 可以理解为左闭右开
        inorder_right = inorder[seperator_idx + 1:]  # 把索引为seperator_idx+1 对应的元素 到最后一个元素赋给新数组。 相当于把中节点挖掉了。

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder) - 1]  # 也是把上个 递归的中节点去掉。

        # 书写左右子树的 递归单层逻辑
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root