#思路一层层遍历每一步可能走的路，直到有一个路最先走到结果
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = list()
        q.append([n,0])
        visited = [False for _ in range(n+1)]#避免重复推入同样的元素
        visited[n] = True
        while q!= None:
            num,step = q.pop(0)
            i = 1
            temp  = num - i**2
            while temp>=0:
                if temp == 0:
                    return step+1
                if not visited[temp]:
                    q.append([temp,step+1])
                    visited[temp] = True
                    
                i += 1
                temp = num - i**2        
