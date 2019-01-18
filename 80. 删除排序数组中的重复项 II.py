class Solution:
    def removeDuplicates(self, nums):
            i  = 2
            nums_len = len(nums)
            while i < nums_len:
                if nums[i] == nums[i-2]:
                    nums.remove(nums[i-2])
                    nums_len = nums_len - 1
                else:
                    i = i+1
            return len(nums)   
