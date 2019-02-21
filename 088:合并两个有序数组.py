class Solution:
    def merge(self, nums1, m, nums2, n):
        for j in range(len(nums2)):
            nums1.pop()
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
