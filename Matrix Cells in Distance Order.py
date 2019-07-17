import queue

class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        self.ans = []
        self.visited = set()
        self.q = queue.Queue()
        self.bfs(r0, c0, R, C)
        return self.ans

    def bfs(self, row, column, R, C):
        self.q.put((row, column))
        self.visited.add((row, column))
        while not self.q.empty():
            row, column = self.q.get()
            self.ans.append([row, column])
            for i, j in [(row+1, column), (row, column+1), (row-1, column), (row, column-1)]:
                if self.is_valid(i, j, R, C):
                    self.q.put((i, j))
                    self.visited.add((i, j))

    def is_valid(self, k, v, R, C):
        if k >= R or k < 0 or v >= C or v < 0 or (k, v) in self.visited:
            return False
        return True

R = 2
C = 2
r0 = 0
c0 = 0
s = Solution()
print(s.allCellsDistOrder(R, C, r0, c0))
