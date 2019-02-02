class Solution(object):
    def twoSum(self, nums, target):
        record = {}
        for i in range(len(nums)):
            cop = target-nums[i]
            if cop in record:
                return [record[cop],i]
            record[nums[i]] = i
