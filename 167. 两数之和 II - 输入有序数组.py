#采用对撞指针的思路
class Solution(object):
    def twoSum(self, nums, target):
        j = len(nums)-1
        i = 0
        while (i < len(nums)) and (j>0):
            if nums[i]+nums[j] == target:
                if i+1 < j+1:
                    return i+1,j+1
                else:
                    return j+1,i+1
            elif nums[i] + nums[j]> target:
                j = j -1
            elif nums[i] + nums[j] < target:
                i = i+1
                
