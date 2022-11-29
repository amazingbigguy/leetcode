class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 我们只需要 维护三种金额 的数量： 5、10、20   (实际上甚至都不需要维护 20 的数量，因为我们不用20 找零)
        # 情况一：账单是5，直接收下。
        # 情况二：账单是10，消耗一个5，增加一个10
        # 情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5     （这其中蕴含着贪心策略，因为5美元更加万能，所以需要珍惜使用）
        five,ten,twenty = 0,0,0
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                if five <= 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            if bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    # twenty += 1   # 其实这行代码可以删了，因为记录20已经没有意义了，不会用20来找零. 所以就 这道题目而言，我们并不需要维护 20
                elif five >= 3:
                    five -= 3
                    # twenty += 1
                else:
                    return False
        return True
    