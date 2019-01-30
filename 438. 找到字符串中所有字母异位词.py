class Solution:
# 注意r 和 l顺序 滑动窗口法 以及 字典 counter的用法 setdefault方法
    def findAnagrams(self, s, p):    
        from collections import Counter
        l = 0
        r = -1
        s_len = len(s)
        result = []
        res_dict = {}
        target = Counter(p)
        while l < len(s):
            if r - l + 1 < len(p) and r+1 < len(s):
                res_dict[s[r+1]] = res_dict.setdefault(s[r+1],0) + 1
                r = r+1
            else:
                res_dict[s[l]] -= 1
                if res_dict[s[l]] == 0:
                    res_dict.pop(s[l])
                l = l + 1
            if r-l + 1 == len(p) and res_dict ==  target:
                result.append(l)
        return result        
        
