class Solution:
    def longestIncreasingPath(self, matrix):
        if not any(matrix):
            return 0
        self.matrix = matrix
        self.cache = {}
        self.max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.max = max(self.max, self.dfs(i, j))
        return self.max

    def dfs(self, i, j):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        current = self.matrix[i][j]
        count = 1 + max(
            self.valid(i+1, j, current), self.valid(i, j+1, current),
            self.valid(i-1, j, current), self.valid(i, j-1, current))
        self.cache[(i, j)] = count
        return count


    def valid(self, i, j, current):
        if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0]) and self.matrix[i][j] > current:
            return self.dfs(i, j)
        return 0


nums = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

s = Solution()
print(s.longestIncreasingPath(nums))
