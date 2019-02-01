#map函数的用法
#别的大佬的思路https://blog.csdn.net/qq_17550379/article/details/80586058
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split(' ')
        return map(s.index,s) == map(pattern.find,pattern)
