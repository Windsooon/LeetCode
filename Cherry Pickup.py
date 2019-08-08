class Solution:
    def cherryPickup(self, grid):
        dp = [[[float('-inf')]*len(grid) for i in range(len(grid))] for i in range(len(grid))]
        dp[0][0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                for k in range(len(grid)):
                    if i == j == k == 0:
                        continue
                    if self.is_valid(i, j, k, len(grid)):
                        if grid[i][j] == -1 or grid[k][i+j-k] == -1:
                            continue
                        else:
                            if i == k and j == i+j-k:
                                cherry = grid[i][j]
                            else:
                                cherry = grid[i][j] + grid[k][i+j-k]
                            # A down b down dp[x][y-1][x2] -
                            # A right b right dp[x-1][y][x2-1]  -
                            # A down b right dp[x][y-1][x2-1] -
                            # A right b down dp[x-1][y][x] -
                            dp[i][j][k] = cherry + max(dp[i-1][j][k-1], dp[i][j-1][k], dp[i-1][j][k], dp[i][j-1][k-1])
        return max(0, dp[-1][-1][-1])

    def is_valid(self, i, j, k, length):
        if i+j-k >= length or i+j-k < 0:
            return False
        return True


s = Solution()
grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
assert s.cherryPickup(grid) == 0
grid = [[0, 1, -1], [1, 0, -1], [1, 1,  1]]
assert s.cherryPickup(grid) == 5
grid = [
    [0, 1,  1],
    [0, 1,  0],
    [0, 1,  1],
    [0, 0,  1],
    [0, 0,  1]]
assert s.cherryPickup(grid) == 7
