class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(n,k,path,res,start):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start,n+1):
                dfs(n,k,path+[i],res,i+1#注意必须是i+1而不是start+1)
        res = []
        dfs(n,k,[],res,1)
        return res
                
#剪枝方法
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(n,k,path,res,start):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start,n+2-k+len(path)):
                dfs(n,k,path+[i],res,i+1)
        res = []
        dfs(n,k,[],res,1)
        return res
                
        
