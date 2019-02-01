#主要涉及字典排序 zip函数 二维列表
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        slist = list(s)
        record = {}
        for i in s:
            record[i] = record.setdefault(i,0)+1
        f = zip(record.values(),record.keys())
        sf = sorted(f,reverse = True)
        for i in range(len(sf)):
            result += sf[i][1]*sf[i][0]
        return result
            
        
