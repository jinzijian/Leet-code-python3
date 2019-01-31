class Solution(object):
    def isHappy(self, n):
        d = {}#数组用来判断是否死循环
        while True:
            m = 0
            while n > 0:
                m += (n%10)**2#这两行是如何取出每一位得数
                n //= 10 
            if m in d:
                return False
            if m == 1:
                return True
            d[m] = m
            n = m
