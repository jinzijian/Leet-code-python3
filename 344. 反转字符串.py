class Solution(object):
    def reverseString(self, s):
        i = len(s)-1
        j = 0
        while i>j:
            s[j],s[i] = s[i] , s[j]
            i = i -1
            j = j+1
