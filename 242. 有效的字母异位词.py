class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        if len(s)!= len(t):
            return False
        used1 = {}
        used2 = {}
        for i in s:
            used1[i] = used1.get(i,0)+1#关键步骤如何赋值给字典
        for j in t:
            used2[j] = used2.get(j,0)+1
        if used1 == used2:
            return True
        else:
            return False
        
