class Solution:

    def getdis(self, a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            record = {}
            for j in range(len(points)):
                if i != j:
                    distance = self.getdis(points[i],points[j])
                    count = record.get(distance,0)#dic get用法
                    record[distance] = count+1
            for key in record.keys():#遍历数组 以及注意循环所处的嵌套位置
                res += record[key]*(record[key]-1)
        return res    
                
