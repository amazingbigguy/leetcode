class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        ticket = defaultdict(list)     # 字典的 val 类型为列表，实际存储进列表里面的元素为 字符串
        for item in tickets:
            ticket[item[0]].append(item[1])    # 把 ticket 列表数组里面每一个 列表元素的第一个索引 出发机场 字符串作为 ticket 字典的 key 值，把对应 item[0] 值的 每一个item[1] 项加入到 字典的 val 列表里面。val列表 里面的元素为 字符串，即为 目标机场。
        # 然后再给 每一个出发机场里面的 目标机场，即是 到达机场进行 按照字母大小的排

        # '''
        # tickets_dict里面的内容是这样的
        #  {'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        # '''    
        path = ["JFK"]   # 初始化结果数组
        
        def backtracking(start_point) ->bool:    # 写一个闭包函数，好调用上一层函数的 变量。 
            if len(path) == len(tickets)+1:
                return True
            ticket[start_point].sort()   # 进行一个排序
            for _ in ticket[start_point]:
                end_point = ticket[start_point].pop(0)    # 为了防止 死循环，每每加入一个元素进入 path，都要相应的把 ticket[start_point] 中的元素去除。 这边也是一个有意思的点，那么符合题意的话，defaultdict 就应该是先进先出的 队列式样 的存储方式。
                path.append(end_point)
                if backtracking(end_point):
                    return True     # 我们只要找到一个符合条件的值，那么就可以返回，没有必要彻底遍历完，因为只需要返回 按字母排序 最小的路径 就可以了。
                path.pop()
                ticket[start_point].append(end_point)
            return False    # 如果遍历完 整个字典 都没有找到的话，那么就可以返回 False了，毕竟还是一个 bool 函数。
        backtracking("JFK")
        return path

#  我只能说，这道题目的价值很大，你忍一下。
