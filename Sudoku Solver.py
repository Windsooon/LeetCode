class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        return self.solve(board)

    def solve(self, board):
        if not self.any_dot(board):
            return True
        for k in range(len(board)):
            for v in range(len(board)):
                if board[k][v] == '.':
                    can = self.get_can(board, k, v)
                    if not can:
                        return False
                    for c in can:
                        board[k][v] = c
                        if self.solve(board):
                            return True
                        board[k][v] = '.'
                    return False
        return False

    def any_dot(self, board):
        for b in board:
            if '.' in b:
                return True
        return False

    def get_can(self, board, i, j):
        existed = set()
        existed.update(board[i])
        existed.update(list(zip(*board))[j])
        row = (i // 3) * 3
        column = (j // 3) * 3
        for k in range(row, row+3):
            for v in range(column, column+3):
                existed.add(board[k][v])
        lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        return [i for i in lst if i not in existed]

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# board = [[".","2","6","5",".","1",".","9","."],["5",".",".",".","7","9",".",".","4"],["3",".",".",".","1",".",".",".","."],["6",".",".",".",".",".","8",".","7"],[".","7","5",".","2",".",".","1","."],[".","1",".",".",".",".","4",".","."],[".",".",".","3",".","8","9",".","2"],["7",".",".",".","6",".",".","4","."],[".","3",".","2",".",".","1",".","."]]

s = Solution()
print(s.solveSudoku(board))
