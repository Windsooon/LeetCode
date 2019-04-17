class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        print(self.solve())
    
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1
    
    def solve(self):
        row, col = self.findUnassigned()
        #no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return self.board
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return self.board
                self.board[row][col] = "."
        return False
            
    def isSafe(self, row, col, ch):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False
    
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
       
    def checksquare(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True

# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

board = [[".","2","6","5",".",".",".","9","."],["5",".",".",".","7","9",".",".","4"],["3",".",".",".","1",".",".",".","."],["6",".",".",".",".",".","8",".","7"],[".","7","5",".","2",".",".","1","."],[".","1",".",".",".",".","4",".","."],[".",".",".","3",".","8","9",".","2"],["7",".",".",".","6",".",".","4","."],[".","3",".","2",".",".","1",".","."]]

s = Solution()
s.solveSudoku(board)
