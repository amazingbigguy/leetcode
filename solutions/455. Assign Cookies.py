class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        index = len(s)-1
        for i in range(len(g)-1,-1,-1):   # 先喂饱 大胃口的，大胃口先吃的局部最优原则
            if index >= 0 and s[index] >= g[i]:
                count +=1
                index -=1
        return count

        # g.sort()
        # s.sort()
        # count = 0
        # index = 0
        # for i in range(len(s)):   # 先喂饱 小胃口的，小胃口先吃的局部最优原则
        #     if index <= len(g)-1 and s[i] >= g[index]: 
        #         count +=1
        #         index +=1
        # return count