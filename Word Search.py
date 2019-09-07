class Solution:
    def exist(self, board, word: str) -> bool:
        if not word:
            return True
        elif not any(board):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, word, board):
                        return True
        return False

    def dfs(self, i, j, index, word, board):
        if index == len(word)-1:
            return True
        tem = board[i][j]
        board[i][j] = '#'
        for k, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if self.is_valid(k, v, index+1, board, word):
                if self.dfs(k, v, index+1, word, board):
                    return True
        board[i][j] = tem
        return False

    def is_valid(self, i, j, index, board, word):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[index]:
            return True
        return False



board = [["F","Y","C","E","N","R","D"],["K","L","N","F","I","N","U"],["A","A","A","R","A","H","R"],["N","D","K","L","P","N","E"],["A","L","A","N","S","A","P"],["O","O","G","O","T","P","N"],["H","P","O","L","A","N","O"]]

s = Solution()
# print(s.exist(board, 'ABCCED'))
# print(s.exist(board, 'ABCB'))
# print(s.exist(board, 'SEE'))
print(s.exist(board, 'poland'))
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(s.exist(board, 'ABCCED'))
