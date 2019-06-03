class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        tmp = []
        for i in range(1,len(s)+1):
            left = s[:i]
            right = s[i:]
            if left ==left[::-1]: #如果左侧不是回文的，则舍弃这种尝试
                right = self.partition(right)
                for i in range(len(right)):
                    tmp.append([left]+right[i])
        return tmp
