class Solution(object):#双指针扫描法
    def reverseVowels(self, s):
        string = ["a","e","i","o","u","A","E","I","O","U"]
        s = list(s)#把字符串变成数组去处理
        i = 0
        j = len(s)-1
        while i < j:
            if  (s[j] not in string):
                j = j-1
            if (s[i] not in string):
                i = i + 1
            if (s[i] in string) and (s[j] in string):
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
        return "".join(s)  #把数组变会字符串//注意return 的缩进
