class Solution:
    def __init__(self):
        self.chessboard = []  # 定义全是 某一个值 的二维数组的 python 表达我尚且不是很熟悉。
        self.result = []  # result 实际上是一个 三维数组，用于存放最终的结果

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result.clear()
        self.chessboard = [['.'] * n for _ in range(n)]
        self.backtracking(n, 0)
        return self.result

    def backtracking(self, n, row):
        if row == n:
            # self.result.append(self.chessboard[:])
            # return

            temp_res = []
            for temp in self.chessboard:
                temp_res.append("".join(temp))
            self.result.append(temp_res)
            return  # 这边我是着实不明白为什么 需要另外创立一个 零时数组来存放元素。

        for vol in range(n):
            if self.isvalid(row, vol, n):
                self.chessboard[row][vol] = 'Q'
                self.backtracking(n, row + 1)
                self.chessboard[row][vol] = '.'

    def isvalid(self, row, vol, n) -> bool:
        # 因为 同一行的合法性通过递归里面的for 循环已经排除了，所以只有同一列上面的合法性判断和左右 45°和135° 角上面的 "Q" 值冲突的合法性判断。
        for i in range(row):  # 实际上是做了剪枝的操作， 因为此时的 chessboard 才更新到了 row 上一行的 逻辑。
            if self.chessboard[i][vol] == 'Q':
                return False
        # 判断左上角 45°的冲突情况
        i, j = row - 1, vol - 1
        while i >= 0 and j >= 0:
            if self.chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断右上角 135°的情况
        i, j = row - 1, vol + 1
        while i >= 0 and j < n:
            if self.chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True