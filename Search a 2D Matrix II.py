class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for m in matrix:
            if not m:
                return
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            current = matrix[i][j]
            if current == target:
                return True
            elif current > target:
                j -= 1
            else:
                i += 1
        return False

matrix = []
target = 0
s = Solution()
print(s.searchMatrix(matrix, target))
