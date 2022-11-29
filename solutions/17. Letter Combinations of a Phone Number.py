class Solution:
    # 首先用一个二维数组做映射
    def __init__(self):
        self.res: List[str] = []    # 二维数组 存储最后的结果//  字符串类型的数组的定义不是self.res = []，而是 self.res: List[str] = []  具体为什么需要这么写，我尚且不明白为什么。 
        self.ans: str = ''    # 字符串数组 存储单次结果// 字符串数组 的定义不是 self.str = '' ， 而是 self.answer: str = '' , 具体为什么需要这么写，我尚且不明白为什么。 
        self.letter_map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtracking(digits, 0)
        return self.res


    def backtracking(self, digits, index):
        if index == len(digits):
            self.res.append(self.ans)
            return 
        
        # digit = digits[index] - '0'   # 不需要这么写，因为和 C++ 里面的 映射规则 好像有所不同。
        digit = digits[index]
        letter = self.letter_map[digit]   # letter 是一个字符串的类型。
        for i in range(len(letter)):
            # self.ans.append(letter[i])   # 字符串没有 类似于数组和 栈以及队列的 append和pop 的属性、
            self.ans += letter[i]
            self.backtracking(digits, index+1)
            self.ans = self.ans[:-1]     # 字符串的最后一个 元素舍弃