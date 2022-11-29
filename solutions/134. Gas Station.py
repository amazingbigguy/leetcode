class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 这道题 依然是使用较为巧妙的 贪心算法
        # 遍历算出经过每一个节点 的剩余油量
        cursum = 0        # 从 索引0 开始遍历，一旦 剩余汽油总和 小于零，那么就startpoint 一定是重新从 i+1 开始
        totalsum = 0      #  如果剩余油量总和 都不大与等于零，那么一定不存在 符合题意的 出发节点
        startpoint = 0    # 出发的节点，因为本题是唯一解，所以一旦找到直接返回

        for i in range(len(gas)):
            cursum += gas[i]-cost[i]
            totalsum += gas[i]-cost[i]
            if cursum < 0:      # 这里很妙，找到了第一个连续正值 的节点，那么一定是可以作为起始节点的。很脑筋急转弯的感觉。
                startpoint = i+1
                cursum = 0
        if totalsum < 0: return -1
        return startpoint