class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.check_column(board) and self.check_row(board) and self.check_tube(board)

    def is_valid(self, lst):
        uni_lst = [l for l in lst if l != '.']
        return len(set(uni_lst)) == len(uni_lst)

    def check_row(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def check_column(self, board):
        for column in zip(*board):
            if not self.is_valid(column):
                return False
        return True

    def check_tube(self, board):
        for row in (range(0, 3), range(3, 6), range(6, 9)):
            for column in (range(0, 3), range(3, 6), range(6, 9)):
                if not self.is_valid([board[i][l] for i in row for l in column]):
                    return False
        return True

lst = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
print(s.isValidSudoku(lst))
