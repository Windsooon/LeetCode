class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 1
        matrix = dungeon[-1]
        for i in range(-1, -len(dungeon)-1, -1):
            for j in range(-1, -len(dungeon[0])-1, -1):
                if i == -1 and j == -1:
                    matrix[-1] = max(1, 1-matrix[-1])
                elif i == -1:
                    matrix[j] = max(1, matrix[j+1] - dungeon[i][j])
                elif j == -1:
                    matrix[j] = max(1, matrix[j] - dungeon[i][j])
                else:
                    matrix[j] = max(1, min(matrix[j], matrix[j+1]) - dungeon[i][j])
        return matrix[0]


dungeon = [[0, 0]]
# dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]

s = Solution()
print(s.calculateMinimumHP(dungeon))
