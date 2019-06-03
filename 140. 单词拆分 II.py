class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #dfs
        res = []
        def dfs(idx,temp):
            if idx == len(s):
                res.append(temp[:-1])
            if not self.check(s[idx:],wordDict):
                return 
            for i in range(idx+1,len(s)+1):
                if s[idx:i] in wordDict:
                    dfs(i,temp+s[idx:i]+" ")
        dfs(0,"")
        return res
        
            
        
        
        
        
        
        
    def check(self, s, wordDict):
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]
        
        #真的很难思路是dfs加dp判断
