class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 因为字典中出现的单词可以重复使用，所以是 完全背包问题
        # wordDict 中的所有字符串互不相同
        # 回溯法容易超时。最好的方法还是使用背包来解决。
        # 单词 就是物品，字符串s就是 背包。问能不能用字典中的单词拼出字符串s，就是在问能不能 用物品填满背包
        # 确定dp 数组的含义，dp[j] 字符串长度为j 的话，dp[j] 表示true表示可以拆分为一个或者多个能在字典中出现的单词。
        # 本题 的遍历顺序和 dp 数组的推导方向还是比较特别的
        length = len(s)
        dp = [False]*(length+1)
        dp[0] = True    #dp[0] 本身没有意义，因为字符串s 的长度大于等于1，设置dp[0] = 0 完全是为了 方便 递推公式的进行
        
        # for word in wordDict:   # 我先遍历物品 试一试
        #     for j in range(1,length+1):
        #         if j >= len(word) and dp[j-len(word)] and word == s[j-len(word):j]:
        #             dp[j] = dp[j-len(word)]  
        # return dp[len(s)]
        
# ok, 先放物品不行，因为物品用一次就不会回头继续用了，所以完全背包问题，物品遍历应该放在下一层for循环里面
        for j in range(1,length+1):       # 这次使用先背包后物品， 能够保证物品重复使用， 这也符合完全背包的 内涵
            for word in wordDict:
                if j >= len(word) and dp[j-len(word)] and word == s[j-len(word):j]:
                    dp[j] = dp[j-len(word)]
        return dp[length]