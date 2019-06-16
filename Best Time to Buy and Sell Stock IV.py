class Solution:
    def maxProfit(self, k, prices):
        length = len(prices)
        if length < 2:
            return 0
        max_profit = 0
        if k>=length/2:
            for i in range(1,length):
                max_profit += max(prices[i]-prices[i-1],0)
            return max_profit

        max_global = [[0]*length for _ in range(k+1)]
        max_local = [[0]*length for _ in range(k+1)]

        for j in range(1,length):
            cur_profit = prices[j]-prices[j-1]
            for i in range(1,k+1):
                max_local[i][j] = max( max_global[i-1][j-1]+max(cur_profit,0), max_local[i][j-1] + cur_profit)
                max_global[i][j] = max(max_global[i][j-1], max_local[i][j])
        return max_global[k][-1]

s = Solution()
k = 10000
prices = [106,373,495,46,359,919,906]
assert (s.maxProfit(k, prices)) == 1262
