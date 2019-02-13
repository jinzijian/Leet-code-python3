class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        record = {}
        for i in range(len(C)):
            for j in range(len(D)):
                count = record.get(C[i]+D[j],0)
                record[C[i]+D[j]] = count + 1
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                temp = -A[i]-B[j]
                if temp in record:
                    res += record[temp]
        return res            
        
