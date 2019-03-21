class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def dfs(candidates,target,path,res,last):
            if target == 0:
                res.append(path)
            if candidates and target < candidates[0]:
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    return
                if candidates[i] < last:
                    continue
                if i-1 >= 0 and candidates[i] == candidates[i-1]:
                    continue

                dfs(candidates[i+1:],target-candidates[i],path+[candidates[i]],res,candidates[i])
        res = []
        dfs(candidates,target,[],res,0)
        return res
