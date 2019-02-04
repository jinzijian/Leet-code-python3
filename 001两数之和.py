class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i in range(0,len(nums)):
            temp = target - nums[i]
            if temp in record:# in 是判断键值
                return [i,record[temp]]
            record[nums[i]] = i
