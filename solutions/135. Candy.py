class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 这道题目 用两次贪心算法，一次从左到右 的遍历 右节点 大于左节点 的情况。
        # 第二次 从右向左 的遍历 左节点 大于 右节点的情况，综合考虑两个方向的贪心结果， 确定节点 的糖果数量
        candy = [1]*len(ratings)    # 先确保每一个人都有 至少一颗糖果
        # 从左到右 的前序遍历，确定 第一种贪心 得出 的各个节点糖果数量
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]: 
                candy[i] = candy[i-1]+1   
        
        # 从右到左 的后序遍历， 确定第二种贪心得到 的各个节点的 糖果数量
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1]+1)
        return sum(candy)