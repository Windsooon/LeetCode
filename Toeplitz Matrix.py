class Solution:
    def isToeplitzMatrix(self, matrix):
        self.seen = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in self.seen:
                    if not self.check(i, j, matrix):
                        return False
        return True

    def check(self, i, j, matrix):
        """
        return True if the matrix[i][j]'s diagonals are the same
        else return False
        """
        val = matrix[i][j]
        while i < len(matrix) and j < len(matrix[0]):
            self.seen.add((i, j))
            if matrix[i][j] != val:
                return False
            i += 1
            j += 1
        return True

s = Solution()

matrix = [
  [1,2],
  [2,2]
]
print(s.isToeplitzMatrix(matrix))
