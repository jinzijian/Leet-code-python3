#滑动窗口法
class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = -1
        res = 0
        while l < len(s) :
            if r+1<len(s) and s[r+1] not in s[l:r+1]:
                r = r + 1
            else:
                l = l+1
            res = max(res,r-l+1)   
        return res
                
