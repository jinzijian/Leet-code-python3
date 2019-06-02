class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
        
     #运用异或 a^a = 0 a^0 = a 所以可用来判断重复
