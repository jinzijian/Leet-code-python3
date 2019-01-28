class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()#搞定大小写问题
        string = []#字符串变成数组
        #把标点符号清除
        for c in s:
            if c.isalnum():#isalnum方法检测是否是数字或字母
                string.append(c)
        i, j = 0, len(string)-1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
