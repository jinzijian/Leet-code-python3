class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #动态规划解法 记录下每次能走到的位置
        res = [0]*(len(s)+1)
        res[0] = 1
        if len(s) == 0 or not wordDict:
            return False
        max_stride = max(len(x) for x in wordDict)
        for i in range(1,len(s)+1):
            for j in range(i-max_stride,i):
                if res[j] == 1 and s[j:i] in wordDict:
                    res[i] = 1
        if res[-1] == 1:
            return True
        if res[-1] == 0:
            return False
   #详细思路https://blog.csdn.net/weixin_42771166/article/details/85320822
