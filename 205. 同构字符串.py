class Solution(object):
    def isIsomorphic(self, s, t):
        return map(s.index,s) == map(t.index,t)
        #和290完全一样
