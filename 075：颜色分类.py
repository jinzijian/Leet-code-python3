#方法一 计数排序 时间O(n) 空间O(k)
#三路快排 88 215



#计数排序
class Solution(object):
    def sortColors(self, nums):
        o = 0
        p = 0
        q = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                o = o+1
            if nums[i] == 1:
                p = p+1
            if nums[i] == 2:
                q = q+1
        for j in range(0,o):
            nums[j] = 0
        for j in range(o,o+p):
            nums[j] = 1
        for j in range(o+p,len(nums)):
            nums[j] = 2    
