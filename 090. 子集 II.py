class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def dfs(nums,path,res,last,length):
            if len(path) == length:
                res.append(path)
            for j in range(len(nums)):
                if j-1 >= 0 and nums[j] == nums[j-1]:
                    continue
                dfs(nums[j+1:],path+[nums[j]],res,nums[j],length)
        res = []
        for i in range(len(nums)+1):
            dfs(nums,[],res,0,i)
        return res
        
