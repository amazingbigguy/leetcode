#  这道题目我真的一眼看过去一点儿思路都没有， 我甚至想不到要用递归回溯。
#  方法一： 另外写一个 判断是否为回文串的 函数。
#          即 回溯+函数判断回文串 的方法判断。 

# class Solution:
#     def __init__(self):
#         self.result: List[List[str]] = []   # 定义字符串二维数组，来存储 结果集
#         self.path: List[str] = []          # 定义字符数组 用于存储单条树枝 的遍历
        
#     def partition(self, s: str) -> List[List[str]]:
#         self.result.clear()
#         self.path.clear()      # 清理内存里面的 预存值
#         self.backtracking(s, 0)
#         return self.result


#     def backtracking(self, s: str, index):
#         if index == len(s):    # 是否为回文为 终止条件的 判定
#             self.result.append(self.path[:])
#             return 
#         for i in range(index, len(s)):
#             if not self.isPalindrome(s, index, i):
#                 continue    # 判断是否是回文
#             else:    
#                 self.path.append(s[index:i+1])       
#                 self.backtracking(s, i+1)
#                 self.path.pop()
            

#     def isPalindrome(self, s, start, end) -> bool:
#         i: int = start
#         j: int = end
#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             else:
#                 i += 1
#                 j -= 1
#         return True


#   方法二： 字符串数组的 正反序 判断回文串
class Solution:
    def __init__(self):
        self.result: List[List[str]] = []   # 定义字符串二维数组，来存储 结果集
        self.path: List[str] = []          # 定义字符数组 用于存储单条树枝 的遍历
        
    def partition(self, s: str) -> List[List[str]]:
        self.result.clear()
        self.path.clear()      # 清理内存里面的 预存值
        self.backtracking(s, 0)
        return self.result


    def backtracking(self, s: str, index):
        if index == len(s):    # 是否为回文为 终止条件的 判定
            self.result.append(self.path[:])
            return 
        for i in range(index, len(s)):
            temp = s[index:i+1]
            if temp == temp[::-1]:     # 我才知道还可以这么 判断两个数组是否相等，不仅仅是字符串数组。我以为是要额外写一个函数遍历元素的，
                                       # 没想到直接就能用。 
                self.path.append(s[index:i+1])       
                self.backtracking(s, i+1)
                self.path.pop()
            else:
                continue