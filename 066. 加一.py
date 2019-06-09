class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        digits[l] += 1
        while l > 0:
            if digits[l] == 10:
                digits[l] = 0
                digits[l-1] += 1
            l -= 1
        if digits[0]==10:
            res = []
            res.append(1)
            res.append(0)
            for i in range(1,len(digits)):
                res.append(digits[i])
            return res
        else:
            return digits
            
            
