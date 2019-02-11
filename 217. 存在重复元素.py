class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
    
#方法二
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record[nums[i]] = 0
        return False
