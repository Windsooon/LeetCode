import sys
sys.setrecursionlimit(1500000000)

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def helper(numUsed, need, c):
            if c == len(coins):
                return float('inf')

            if need % coins[c] == 0:
                cand = need // coins[c] + numUsed
                return cand

            for numChosen in range(need // coins[c], -1, -1):
                ret = helper(numUsed + numChosen, need - coins[c] * numChosen, c + 1)
                if ret != float('inf'):
                    return ret
            return ret

        coins = list(sorted([coin for coin in set(coins) if coin > 0], reverse=True))
        ret = helper(0, amount, 0)
        return ret if ret < float('inf') else -1


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def helper(knownBest, numUsed, need, c):
            if need % coins[c] == 0:
                return need // coins[c] + numUsed

            if numUsed - (-need // coins[c]) >= knownBest:
                return float('inf')

            if c == len(coins) - 1:
                return float('inf')

            for numChosen in range(need // coins[c], -1, -1):
                cand = helper(knownBest, numUsed + numChosen, need - coins[c] * numChosen, c + 1)
                if cand < knownBest:
                    knownBest = cand
            return knownBest
        inf = float('inf')
        coins = list(sorted([coin for coin in set(coins) if coin > 0], reverse=True))
        ret = helper(float('inf'), 0, amount, 0)
        return ret if ret < float('inf') else -1

class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse = True)
        lenc, self.res = len(coins), 2**31-1
        a_count = 0
        
        def dfs(pt, rem, count):
            nonlocal a_count
            if not rem:
                self.res = min(self.res, count)
                return
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count):
                    a_count += 1
                    dfs(i, rem-coins[i], count+1)

        for i in range(lenc):
            dfs(i, amount, 0)
        print(a_count)
        return self.res if self.res < 2**31-1 else -1

s = Solution()
# print(s.coinChange([2], 3))
# print(s.coinChange([1, 2, 5], 11))
# print(s.coinChange([1, 2, 5], 100))
# print(s.coinChange([3,7,405,436], 8839))
s.coinChange([186,419,83,408], 6249)
s.coinChange([1,2,3,400], 6249)
# print(s.coinChange([1,2,3,4], 9999))
