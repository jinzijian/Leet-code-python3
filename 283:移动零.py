class Solution:
    def moveZeroes(self, nums):
            k = 0
            nums_len = len(nums)
            for i in range(nums_len):
                if (nums[i] != 0):
                    nums[k] = nums[i]
                    k = k+1
            for j in range(k,nums_len):
                nums[j] = 0
