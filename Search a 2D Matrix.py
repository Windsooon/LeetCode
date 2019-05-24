class Solution:
    def searchMatrix(self, matrix, target):
        if not any(matrix):
            return False
        line = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                line = i
        if line == -1:
            return False
        return self.binary_search(matrix[line], target)

    def binary_search(self, line, target):
        left, right = 0, len(line)-1
        while left <= right:
            mid = (left+right)//2
            if line[mid] == target:
                return True
            elif line[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

s = Solution()

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 13))
