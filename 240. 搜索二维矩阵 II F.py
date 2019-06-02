未能独立写出
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = -1
        for row in matrix:
            while j > -len(row) and row[j] > target:
                j -= 1
            if row and row[j] == target:
                return True
        return False
 思路
 从矩阵右上角开始，若值比 target 大则证明这一列的值都比 target 大，继续搜索前面的列；若比 target 小说明 target 可能在后面的行中，进入下一行
