class Solution:
#字典的基本操作 和注意条件 注意if后面的问题
    def intersect(self, nums1, nums2):
        record = {}
        result = []
        for i in range(len(nums1)):
            if record.has_key(nums1[i]):
                record[nums1[i]] += 1
            else:
                record[nums1[i]] = 1
        for j in range(len(nums2)):
            if record.has_key(nums2[j]) and record[nums2[j]] > 0:
                record[nums2[j]] -= 1
                result.append(nums2[j])
        return result        
