class Solution:
    def uniquePathsIII(self, grid):
        if not any(grid):
            return 0
        # search start point
        self.ans = 0
        count, i, j = self.search(grid)
        self.dfs(i, j, grid, count)
        return self.ans

    def search(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    count += 1
        return count, x, y


    def dfs(self, i, j, grid, count):
        if grid[i][j] == 2:
            if count == -1:
                self.ans += 1
            return
        current = grid[i][j]
        grid[i][j] = '#'
        for v, k in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
            if self.valid(v, k, grid):
                self.dfs(v, k, grid, count-1)
        grid[i][j] = current

    def valid(self, i, j, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != '#' and grid[i][j] != -1:
            return True
        return False

grid = [[0,1],[2,0]]
s = Solution()
print(s.uniquePathsIII(grid))
