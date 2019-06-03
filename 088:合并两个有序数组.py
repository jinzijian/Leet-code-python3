class Solution:
    def merge(self, nums1, m, nums2, n):
        for j in range(len(nums2)):
            nums1.pop()
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()

        
        
        
        
  class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #倒着排序的方法
        while n>0:
#             if m and nums1[m-1] > nums2[n-1]:#疑问循环条件？？？？
                nums1[m+n-1] = nums1[m-1]
                m = m-1
            else:
                nums1[m+n-1] = nums2[n-1]
                n = n-1
        return nums1
        
        
