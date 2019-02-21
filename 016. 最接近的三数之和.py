class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = nums[j]+nums[i]+nums[k]
                if ans is None or abs(target - temp) < abs(target-ans):
                    ans = temp
                if temp <= target:
                    j += 1
                else:
                    k -= 1
        return ans           
           #双指针法
