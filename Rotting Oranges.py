class Solution:
    def orangesRotting(self, grid):
        fresh_count, rotten_positions = self.fresh_and_rotten(grid)
        became_rotten, time = self.bfs(grid, rotten_positions)
        if fresh_count != became_rotten:
            return -1
        return time
        
    def fresh_and_rotten(self, grid):
        count = 0
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    res.append((i, j))
        return count, res
    
    def bfs(self, grid, rotten_positions):
        time = 0
        count = 0
        while rotten_positions:
            tem = []
            for r, c in rotten_positions:
                for k, v in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if self.isvalid(k, v, grid) and grid[k][v] == 1:
                        grid[k][v] = 2
                        count += 1
                        tem.append((k, v))
            time += 1
            rotten_positions = tem
        return count, time
    
    def isvalid(self, k, v, grid):
        if 0 <= k < len(grid) and 0 <= v < len(grid[0]):
            return True
        return False

s = Solution()
s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
