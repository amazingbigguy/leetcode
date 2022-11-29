class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 完了，我现在做题 是完全没有思路的
        # 但是我还是 对于python 中的hash 太不熟悉了
        hash = [0]*26
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')] = i   #  记录某一个确定字母 最后出现的位置
        
        result = []
        left,right = 0,0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i])-ord('a')])    # 更新遍历到 的字母 的最远边界
            if i == right:
                result.append(right-left+1)   # 这里不是很理解
                left = i+1
        return result