class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        j = 0
        i = len(nums)
        while i > 0:
            i = i-1
            j = j+1
            if j == k:
                break
        return nums[i]           
            
