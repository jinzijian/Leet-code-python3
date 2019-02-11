#滑动窗口+字典
#通过控制record大小 来控制滑动窗口
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record[nums[i]] = 0
            if len(record) == k+1:
                record.pop(nums[i-k])
        return False        
