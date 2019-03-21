class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(n,k,path,res,start):
            if len(path) == k and n == 0:
                res.append(path)
            for i in range(start,10):
                if i > n:
                    return
                dfs(n-i,k,path+[i],res,i+1)
        res = []
        dfs(n,k,[],res,1)
        return res
            
