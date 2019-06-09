class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        row = defaultdict(set)
        col = defaultdict(set)
        square =defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in square[(i//3,j//3)]:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        square[(i//3,j//3)].add(board[i][j])
                    else:
                        return False
        print(row[1])
        return True
