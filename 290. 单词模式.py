#map函数的用法
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split(' ')
        return map(s.index,s) == map(pattern.find,pattern)
