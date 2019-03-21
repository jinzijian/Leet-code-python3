#思路https://blog.csdn.net/zl87758539/article/details/51693179
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,target,path,res,last):
            if target == 0:
                res.append(path)
            if target < candidates[0]:
                return
            for n in candidates:
                if n > target:
                    return
                if n<last:
                    continue
                dfs(candidates,target-n,path+[n],res,n)
                
                
        
        
        
        candidates.sort()
        res = []
        dfs(candidates,target,[],res,0)
        return res
