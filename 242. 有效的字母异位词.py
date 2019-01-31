class Solution(object):
    def isAnagram(self, s, t):
        record = {}
        if len(s) < len(t):
            a = s
            s = t
            t = a
        for i in s:
            record[i] = record.setdefault(i,0) + 1
        for j in t:
            if j in record:
                record[j] -= 1
                if record[j] == 0:
                    record.pop(j)
        if record =={}:
            return True
        else:
            return False
        
