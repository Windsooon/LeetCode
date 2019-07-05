import queue
class Solution:
    def swimInWater(self, grid):
        dis_grid = [[float('inf')] * len(grid[0]) for i in range(len(grid))]
        self.visited = {}
        q = queue.PriorityQueue()
        # sorted by time
        self.visited[(0, 0)] = True
        q.put((grid[0][0], 0, 0))
        while not q.empty():
            time, i, j = q.get()
            for k, v in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if self.valid(k, v, grid) and (k, v) not in self.visited:
                    dis_grid[k][v] = min(max(time, grid[k][v]), dis_grid[k][v])
                    self.visited[(k, v)] = True
                    q.put((dis_grid[k][v], k, v))
        return dis_grid[-1][-1]

    def valid(self, i, j, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            return True
        return False


s = Solution()
grid = [[0,2],[1,3]]
grid = [[26,99,80,1,89,86,54,90,47,87],[9,59,61,49,14,55,77,3,83,79],[42,22,15,5,95,38,74,12,92,71],[58,40,64,62,24,85,30,6,96,52],[10,70,57,19,44,27,98,16,25,65],[13,0,76,32,29,45,28,69,53,41],[18,8,21,67,46,36,56,50,51,72],[39,78,48,63,68,91,34,4,11,31],[97,23,60,17,66,37,43,33,84,35],[75,88,82,20,7,73,2,94,93,81]]
print(s.swimInWater(grid))
