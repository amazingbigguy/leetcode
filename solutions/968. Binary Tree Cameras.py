class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 这道题目 真的没有思路......
        # OK，看了解析，思路来了。
        # 首先是 判断出 叶子节点不放摄像头，那么空节点 一定是 不放摄像头但是有覆盖的情况，这样才能保证 叶子节点 的父节点放置 摄像头的时候，保证整颗 二叉树的摄像头 数量是最小的。
        # 我们用 三个数字来表示 三种情况 
        # 0：该节点无覆盖
        # 1：本节点有摄像头
        # 2：本节点有覆盖
        result = 0
        def traversal(node):
            nonlocal result
            # 空节点应该 是有覆盖的情况
            if not node:
                return 2
            left = traversal(node.left)
            right = traversal(node.right)

            # 相当于表达叶子节点，（目前）应该是没有覆盖，也不该设置 摄像头的状态
            if left == 2 and right == 2:
                return 0
            # 只要 左右节点有一个 是没有覆盖的情况，就都应该 把父节点设施为 1
            if left == 0 or right == 0:
                result +=1
                return 1
            # 因为（1，0）和（0,1） 的情况都讨论过了，不会到进行到这一步的 逻辑判断中来，
            # 所有 这个条件表达的是 左右孩子只要有一个 是有摄像头的，那么父节点也应该被覆盖了
            if left == 1 or right == 1:
                return 2
        # 如果头结点 的左右孩子都为 2的话，那么头结点是应该放置 摄像头的，这种遗漏的情况需要考虑上去。
        if traversal(root) == 0:
            result += 1
        return result