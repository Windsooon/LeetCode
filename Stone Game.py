import functools

class Solution:
    def stoneGame(self, piles):
        self.piles = piles
        best_move = self.move(0, len(piles)-1)
        return best_move > (sum(piles) - best_move)

    @functools.lru_cache(None)
    def move(self, start, end):
        if start > end:
            return 0
        if start == end:
            return self.piles[start]
        elif end - start == 1:
            return max(self.piles[end], self.piles[start])
        first = self.piles[start] + sum(self.piles[start+1:end+1]) - self.move(start+1, end)
        last = self.piles[end] + sum(self.piles[start:end]) - self.move(start, end-1)
        return max(first, last)

s = Solution()
print(s.stoneGame([3,2,10,4]))
