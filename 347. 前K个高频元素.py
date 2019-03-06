#利用了heapq的结构
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0)+1
        pq = list()
        for key,value in dict.items():
            if len(pq)<k:
                heapq.heappush(pq,(value,key))
            elif value > pq[0][0]:
                heapq.heapreplace(pq,(value,key))
        res = list()
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res
