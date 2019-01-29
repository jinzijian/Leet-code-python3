class Solution:#滑动窗口经典题
    def minSubArrayLen(self, s, nums):
        l = 0
        r = -1
        sum = 0
        res = len(nums)+1
        while l < len(nums):
            if sum < s and r+1 < len(nums):
                r = r+1
                sum = sum + nums[r]
            else:
                sum = sum - nums[l]
                l = l+1
            if sum >= s:
                res = min(res,r-l+1)
        if res == len(nums)+1 or len(nums)==0:
            return 0
        else:
            return res
                
