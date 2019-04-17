class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for i in range(n)]
        # ['...',
        #  '...',
        #  '...']
        self.ans = []
        self.dfs(board, n, 0)
        return self.ans

    def dfs(self, board, n, index):
        if index == n:
            self.ans.append([''.join(b) for b in board])
            return
        for i in range(n):
            board[index][i] = 'Q'
            if self.is_valid(board, index, i, n):
                self.dfs(board, n, index+1)
            board[index][i] = '.'

    def is_valid(self, board, x, y, n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q' and (i + j == x + y or i - j == x - y or j == y) and (i, j) != (x, y):
                    return False
        return True


s = Solution()
print(s.solveNQueens(4))
