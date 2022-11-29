class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result.clear()
        if len(s) < 4 or len(s) > 12:
            return []
        self.backtracking(s, 0, 0)
        return self.result

    
    def backtracking(self, s: str, index, pointsum):
        if pointsum == 3:
            if self.isValid(s, index, len(s)-1):
                self.result.append(s[:])
            return

        for i in range(index, len(s)):
            if self.isValid(s, index, i):
                s = s[:i+1]+'.'+s[i+1:]
                pointsum += 1
                self.backtracking(s, i+2, pointsum) 
                pointsum -= 1
                s = s[:i+1]+s[i+2:]
            else:
                break   # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环




    def isValid(self, s, start, end) -> bool:
        if start > end:
            return False
        if s[start] == '0' and end > start:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True