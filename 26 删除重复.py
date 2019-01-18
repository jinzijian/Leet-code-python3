#笨蛋方法会超出时间限制
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        if len(nums) == 0:
            return 0
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[i])
                j = j + 1
                i = i + 1
        return len(nums)
       
       
# solution2 普通方法
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                continue
            i = i + 1

        return len(nums)

#利用set方法 优化
class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(list(set(nums)))
        if len(l):
            for i in range(0, len(l)):
                nums[i] = l[i]
        return len(l)
